from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
from dateutil.relativedelta import relativedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    target_discount_percentage = fields.Float(
        string='Target Discount (%)',
        default=0,
    )
    target_discount_amount = fields.Monetary(
        string='Target Discount Amount',
        default=0,
    )
    historical_invoice_total = fields.Monetary(
        string='Historical Invoice Total',
        default=0,
    )
    has_target_discount = fields.Boolean(
        compute='_compute_has_target_discount',
    )

    def _get_active_discount_config(self):
        return self.env['target.discount.config'].search([
            ('active', '=', True),
            ('company_id', '=', self.company_id.id),
        ], limit=1)

    def _check_order_date_matches_config(self, config):
        order_date = self.date_order.date() if self.date_order else fields.Date.today()
        if config.period_type == 'yearly':
            return order_date.year == config.year
        else:
            month = int(config.month)
            return order_date.year == config.year and order_date.month == month

    def _get_customer_historical_invoices(self, partner, config):
        if not partner or not config:
            return self.env['account.move']

        commercial_partner = partner.commercial_partner_id or partner
        domain = [
            '|',
            ('partner_id', '=', commercial_partner.id),
            ('partner_id.commercial_partner_id', '=', commercial_partner.id),
            ('move_type', 'in', ['out_invoice', 'out_refund']),
            ('state', '=', 'posted'),
            ('company_id', '=', self.company_id.id),
        ]

        if config.period_type == 'yearly':
            start_date = date(config.year, 1, 1)
            end_date = date(config.year, 12, 31)
        else:
            month = int(config.month)
            start_date = date(config.year, month, 1)
            end_date = start_date + relativedelta(months=1, days=-1)

        domain += [
            ('invoice_date', '>=', start_date),
            ('invoice_date', '<=', end_date),
        ]

        return self.env['account.move'].search(domain)

    def _calculate_historical_discount(self):
        """Calculate historical invoice total and discount percentage based on partner."""
        self.ensure_one()
        self.historical_invoice_total = 0.0
        self.target_discount_percentage = 0.0
        self.target_discount_amount = 0.0

        if not self.partner_id:
            return

        config = self._get_active_discount_config()
        if not config:
            return

        if not self._check_order_date_matches_config(config):
            return

        invoices = self._get_customer_historical_invoices(self.partner_id, config)
        historical_total = sum(inv.amount_total_signed for inv in invoices)
        self.historical_invoice_total = historical_total

        discount_percentage = config.get_discount_percentage(historical_total)
        self.target_discount_percentage = discount_percentage

    def _calculate_discount_amount(self):
        """Calculate discount amount based on current order lines."""
        self.ensure_one()
        if self.target_discount_percentage <= 0:
            self.target_discount_amount = 0.0
            return

        subtotal = sum(
            line.price_subtotal
            for line in self.order_line
            if not line.is_target_discount_line
        )
        self.target_discount_amount = subtotal * (self.target_discount_percentage / 100)

    def _compute_has_target_discount(self):
        for order in self:
            order.has_target_discount = any(
                line.is_target_discount_line for line in order.order_line
            )

    def _get_discount_product(self):
        product = self.env['product.product'].search([
            ('is_target_discount', '=', True),
        ], limit=1)
        if not product:
            raise UserError(_('Please create a Target Discount Product with "Is Target Discount Product" checked.'))
        return product

    def _get_target_discount_account(self):
        self.ensure_one()
        config = self._get_active_discount_config()
        if config and config.discount_account_id:
            return config.discount_account_id
        return False

    def action_apply_target_discount(self):
        """Apply discount as a negative product line to deduct from order total."""
        self.ensure_one()
        self._calculate_discount_amount()

        if self.target_discount_percentage <= 0:
            return

        existing_discount_lines = self.order_line.filtered(lambda l: l.is_target_discount_line)
        existing_discount_lines.unlink()

        discount_product = self._get_discount_product()
        if not discount_product:
            return

        discount_account = self._get_target_discount_account()
        if not discount_account:
            raise UserError(_('Please configure a Discount Account on the Sale Type or Target Discount Configuration.'))

        discount_amount = self.target_discount_amount

        self.env['sale.order.line'].create({
            'order_id': self.id,
            'product_id': discount_product.id,
            'name': _('Target Discount (%(percentage)s%%)', percentage=self.target_discount_percentage),
            'product_uom_qty': 1,
            'price_unit': -discount_amount,
            'is_target_discount_line': True,
            'discount_account_id': discount_account.id,
        })

    def action_remove_target_discount(self):
        """Remove discount line from order."""
        self.ensure_one()
        discount_lines = self.order_line.filtered(lambda l: l.is_target_discount_line)
        discount_lines.unlink()
        self.target_discount_amount = 0.0

    @api.onchange('partner_id')
    def _onchange_partner_calculate_discount(self):
        self._calculate_historical_discount()

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        for order in orders:
            if order.partner_id:
                order._calculate_historical_discount()
        return orders

    def write(self, vals):
        res = super().write(vals)
        if 'partner_id' in vals:
            for order in self:
                order._calculate_historical_discount()
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_target_discount_line = fields.Boolean(
        string='Is Target Discount Line',
        default=False,
    )
    discount_account_id = fields.Many2one(
        'account.account',
        string='Discount Account',
    )

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        if self.is_target_discount_line and self.discount_account_id:
            res['account_id'] = self.discount_account_id.id
        return res
