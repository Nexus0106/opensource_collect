# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NrcPrefix(models.Model):
    _name = 'nrc.prefix'
    _description = 'NRC State/Region Prefix'
    _order = 'code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='State/Region Name', required=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code))
        return result
