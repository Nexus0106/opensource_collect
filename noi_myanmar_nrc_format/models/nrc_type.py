# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NrcType(models.Model):
    _name = 'nrc.type'
    _description = 'NRC Citizenship Type'
    _order = 'sequence, code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Type Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code))
        return result
