# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nrc_prefix_id = fields.Many2one('nrc.prefix', string='NRC State/Region')
    nrc_township_code_id = fields.Many2one(
        'nrc.township.code',
        string='NRC Township',
        domain="[('prefix_id', '=', nrc_prefix_id)]"
    )
    nrc_type_id = fields.Many2one('nrc.type', string='NRC Type')
    nrc_number = fields.Char(string='NRC Number', size=6)
    nrc = fields.Char(string='NRC', compute='_compute_nrc', store=True)

    @api.depends('nrc_prefix_id', 'nrc_township_code_id', 'nrc_type_id', 'nrc_number')
    def _compute_nrc(self):
        for record in self:
            if record.nrc_prefix_id and record.nrc_township_code_id and record.nrc_type_id and record.nrc_number:
                record.nrc = '%s/%s(%s)%s' % (
                    record.nrc_prefix_id.code,
                    record.nrc_township_code_id.code,
                    record.nrc_type_id.code,
                    record.nrc_number
                )
            else:
                record.nrc = False

    @api.onchange('nrc_prefix_id')
    def _onchange_nrc_prefix_id(self):
        self.nrc_township_code_id = False
