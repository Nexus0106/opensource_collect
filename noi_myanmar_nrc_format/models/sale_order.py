from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    nrc_prefix_id = fields.Many2one("nrc.prefix", string="NRC Prefix")
    nrc_township_code_id = fields.Many2one(
        "nrc.township.code",
        string="NRC Township",
        domain="[('prefix_id', '=', nrc_prefix_id)]",
    )
    nrc_type_id = fields.Many2one("nrc.type", string="NRC Type")
    nrc_number = fields.Char(string="NRC Number", size=6)
    nrc_full = fields.Char(string="Full NRC", compute="_compute_nrc_full", store=True)

    @api.depends("nrc_prefix_id", "nrc_township_code_id", "nrc_type_id", "nrc_number")
    def _compute_nrc_full(self):
        for order in self:
            if order.nrc_prefix_id and order.nrc_township_code_id and order.nrc_type_id and order.nrc_number:
                order.nrc_full = "{}/{}({}){}".format(
                    order.nrc_prefix_id.code or "",
                    order.nrc_township_code_id.code or "",
                    order.nrc_type_id.code or "",
                    order.nrc_number or "",
                )
            else:
                order.nrc_full = False

    @api.onchange("nrc_prefix_id")
    def _onchange_nrc_prefix_id(self):
        self.nrc_township_code_id = False
