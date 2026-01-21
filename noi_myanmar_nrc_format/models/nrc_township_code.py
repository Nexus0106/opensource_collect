from odoo import api, fields, models


class NrcTownshipCode(models.Model):
    _name = "nrc.township.code"
    _description = "NRC Township Code"
    _order = "prefix_id, code"
    _rec_name = "code"

    name = fields.Char(string="Township Name", required=True)
    code = fields.Char(string="Code", required=True)
    prefix_id = fields.Many2one("nrc.prefix", string="NRC Prefix", required=True, ondelete="restrict")
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("prefix_code_unique", "unique(prefix_id, code)", "Township code must be unique per NRC Prefix!"),
    ]

    @api.depends("name", "code", "prefix_id")
    def _compute_display_name(self):
        for record in self:
            if record.prefix_id and record.code and record.name:
                record.display_name = f"{record.prefix_id.code}/{record.code} - {record.name}"
            else:
                record.display_name = record.name or record.code

    @api.model
    def _name_search(self, name, domain=None, operator="ilike", limit=None, order=None):
        domain = domain or []
        if name:
            domain = ["|", "|", ("code", operator, name), ("name", operator, name), ("prefix_id.code", operator, name)] + domain
        return self._search(domain, limit=limit, order=order)
