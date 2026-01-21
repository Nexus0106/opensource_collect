from odoo import api, fields, models


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
        (
            "prefix_code_unique",
            "unique(prefix_id, code)",
            "Township code must be unique per prefix!",
        ),
    ]

    @api.depends("name", "code", "prefix_id")
    def _compute_display_name(self):
        for record in self:
            prefix = record.prefix_id.code or ""
            record.display_name = f"{prefix}/{record.code} - {record.name}" if record.code else record.name

    @api.model
    def _rec_names_search(self, name="", operator="ilike", limit=100, **kwargs):
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("code", operator, name)]
        return self._search(domain, limit=limit)
