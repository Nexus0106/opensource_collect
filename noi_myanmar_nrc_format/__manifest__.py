{
    "name": "Myanmar NRC Format",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "summary": "Myanmar National Registration Card format for Sales Orders",
    "description": """
Myanmar NRC Format
==================
This module adds Myanmar NRC (National Registration Card) fields to Sale Orders.

Features:
- NRC Prefix (State/Division codes)
- NRC Township Codes
- NRC Types (N, E, P, etc.)
- Full NRC number composition on Sale Orders
    """,
    "author": "ZbyE Solution",
    "maintainer": "ZbyE Solution",
    "website": "nexorionis.odoo.com",
    "support": "zbye.info@gmail.com",
    "images": ["static/description/banner.png"],
    "license": "LGPL-3",
    "depends": ["base","contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/nrc_prefix_data.xml",
        "data/nrc_township_code_data.xml",
        "data/nrc_type_data.xml",
        "views/nrc_prefix_views.xml",
        "views/nrc_township_code_views.xml",
        "views/nrc_type_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
