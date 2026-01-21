from odoo import api, fields, models


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

    @api.depends("name", "code")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.code} - {record.name}" if record.code and record.name else record.name or record.code

    @api.model
    def _name_search(self, name, domain=None, operator="ilike", limit=None, order=None):
        domain = domain or []
        if name:
            domain = ["|", ("code", operator, name), ("name", operator, name)] + domain
        return self._search(domain, limit=limit, order=order)
