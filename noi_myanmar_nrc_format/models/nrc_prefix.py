from odoo import fields, models


class NrcPrefix(models.Model):
    _name = "nrc.prefix"
    _description = "NRC Prefix (State/Division Code)"
    _order = "code"
    _rec_name = "code"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_unique", "unique(code)", "NRC Prefix code must be unique!"),
    ]
