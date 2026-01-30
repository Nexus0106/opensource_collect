# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_target_discount = fields.Boolean(
        string='Is Target Discount Product',
        default=False,
        help='Check this box to mark this product as the Target Discount product.',
    )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_target_discount = fields.Boolean(
        string='Is Target Discount Product',
        related='product_tmpl_id.is_target_discount',
        store=True,
        readonly=False,
    )
