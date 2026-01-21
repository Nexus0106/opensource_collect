from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nrc_prefix_id = fields.Many2one('nrc.prefix', string="NRC Prefix")
    nrc_township_code_id = fields.Many2one(
        'nrc.township.code',
        string="NRC Township Code",
        domain="[('prefix_id', '=', nrc_prefix_id)]"
    )
    nrc_type_id = fields.Many2one('nrc.type', string="NRC Type")
    nrc_number = fields.Char(string="NRC Number (6 digits)")
    nrc = fields.Char(string="NRC", compute='_compute_nrc', store=True)

    @api.depends('nrc_prefix_id', 'nrc_township_code_id', 'nrc_type_id', 'nrc_number')
    def _compute_nrc(self):
        for rec in self:
            if rec.nrc_prefix_id and rec.nrc_township_code_id and rec.nrc_type_id and rec.nrc_number:
                rec.nrc = f"{rec.nrc_prefix_id.code}/{rec.nrc_township_code_id.code}({rec.nrc_type_id.code}){rec.nrc_number}"
            else:
                rec.nrc = False

    @api.onchange('nrc_prefix_id')
    def _onchange_nrc_prefix_id(self):
        self.nrc_township_code_id = False
