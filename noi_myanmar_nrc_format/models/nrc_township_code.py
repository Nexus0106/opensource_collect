from odoo import fields, models


class NrcTownshipCode(models.Model):
    _name = "nrc.township.code"
    _description = "NRC Township Code"
    _order = "prefix_id, code"
    _rec_name = "code"

    name = fields.Char(string="Township Name", required=True)
    code = fields.Char(string="Code", required=True)
    prefix_id = fields.Many2one("nrc.prefix", string="NRC Prefix", required=True, ondelete="cascade")
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("prefix_code_unique", "unique(prefix_id, code)", "Township code must be unique per prefix!"),
    ]
