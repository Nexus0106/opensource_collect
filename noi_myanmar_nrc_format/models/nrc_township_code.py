from odoo import models, fields


class NrcTownshipCode(models.Model):
    _name = 'nrc.township.code'
    _description = 'NRC Township Code'
    _order = 'prefix_id, code'
    _rec_name = "code"

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name')
    prefix_id = fields.Many2one('nrc.prefix', string='Prefix', required=True, ondelete='cascade')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_prefix_unique', 'unique(code, prefix_id)', 'Township code must be unique per prefix!')
    ]

    def name_get(self):
        return [(rec.id, rec.code) for rec in self]
