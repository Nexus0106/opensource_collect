from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TargetDiscountConfig(models.Model):
    _name = 'target.discount.config'
    _description = 'Target Discount Configuration'
    _order = 'id desc'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    period_type = fields.Selection([
        ('yearly', 'Yearly'),
        ('monthly', 'Monthly'),
    ], string='Period Type', required=True, default='yearly')
    year = fields.Integer(string='Year', required=True, default=lambda self: fields.Date.today().year)
    month = fields.Selection([
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ], string='Month')
    discount_account_id = fields.Many2one(
        'account.account',
        string='Discount Account',
        help='Contra-revenue account for discount journal entries',
        required=True,
    )
    slab_ids = fields.One2many(
        'target.discount.slab',
        'config_id',
        string='Discount Slabs',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
    )

    @api.constrains('active')
    def _check_single_active(self):
        for record in self:
            if record.active:
                active_configs = self.search([
                    ('active', '=', True),
                    ('company_id', '=', record.company_id.id),
                    ('id', '!=', record.id),
                ])
                if active_configs:
                    raise ValidationError(_('Only one active Target Discount Configuration is allowed per company.'))

    @api.constrains('period_type', 'month')
    def _check_month_required(self):
        for record in self:
            if record.period_type == 'monthly' and not record.month:
                raise ValidationError(_('Month is required for monthly period type.'))

    def get_discount_percentage(self, amount):
        self.ensure_one()
        discount_percentage = 0.0
        for slab in self.slab_ids.sorted(key=lambda s: s.min_amount):
            if amount >= slab.min_amount:
                discount_percentage = slab.discount_percentage
        return discount_percentage


class TargetDiscountSlab(models.Model):
    _name = 'target.discount.slab'
    _description = 'Target Discount Slab'
    _order = 'min_amount'

    config_id = fields.Many2one(
        'target.discount.config',
        string='Configuration',
        required=True,
        ondelete='cascade',
    )
    min_amount = fields.Float(string='Minimum Amount', required=True)
    discount_percentage = fields.Float(string='Discount (%)', required=True)

    @api.constrains('min_amount', 'discount_percentage')
    def _check_values(self):
        for record in self:
            if record.min_amount < 0:
                raise ValidationError(_('Minimum amount cannot be negative.'))
            if record.discount_percentage < 0 or record.discount_percentage > 100:
                raise ValidationError(_('Discount percentage must be between 0 and 100.'))
