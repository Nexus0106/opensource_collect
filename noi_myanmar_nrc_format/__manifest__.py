{
    "name": "Myanmar NRC Format",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "summary": "Myanmar National Registration Card format for Sale Orders",
    "description": """
Myanmar NRC Format
==================
This module adds Myanmar NRC (National Registration Card) format support
to Sale Orders with proper validation.

Features:
- NRC Prefix (State/Division codes)
- NRC Township Codes
- NRC Types (Naing, Pyuu, Ae, etc.)
- Complete NRC field on Sale Order(Example)
    """,
    "author": "NexOrioins Techsphere",
    "maintainer": "Rowan Ember",
    "website": "nexorionis.odoo.com",
    "support": "nexorionis.info@gmail.com",
    "images": ["static/description/banner.png"],
    "license": "LGPL-3",
    "depends": ["contacts","base"],
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
