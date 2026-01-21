from odoo import models, fields


class NrcPrefix(models.Model):
    _name = 'nrc.prefix'
    _description = 'NRC Prefix (State/Region Code)'
    _order = 'code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'NRC Prefix code must be unique!')
    ]

    def name_get(self):
        return [(rec.id, rec.code) for rec in self]
