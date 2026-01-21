# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NrcTownshipCode(models.Model):
    _name = 'nrc.township.code'
    _description = 'NRC Township Code'
    _order = 'prefix_id, code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Township Name', required=True)
    prefix_id = fields.Many2one('nrc.prefix', string='State/Region', required=True, ondelete='cascade')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code))
        return result
