from odoo import fields, models


class NrcType(models.Model):
    _name = "nrc.type"
    _description = "NRC Type"
    _order = "code"
    _rec_name = "code"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_unique", "unique(code)", "NRC Type code must be unique!"),
    ]
