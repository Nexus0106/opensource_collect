from odoo import models, fields


class NrcType(models.Model):
    _name = 'nrc.type'
    _description = 'NRC Citizenship Type'
    _order = 'sequence, code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'NRC Type code must be unique!')
    ]

    def name_get(self):
        return [(rec.id, rec.code) for rec in self]
