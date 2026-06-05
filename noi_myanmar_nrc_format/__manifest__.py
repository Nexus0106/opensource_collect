{
    "name": "Myanmar NRC Format",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "summary": "Myanmar National Registration Card Format for Sales Orders",
    "description": """
        This module adds Myanmar NRC (National Registration Card) format support.
        Features:
        - NRC Prefix (State/Division codes)
        - NRC Township Codes
        - NRC Types (N, E, P, etc.)
        - Integration with Sale Orders
    """,
    "author": "ZbyE Solution",
    "company": "ZbyE Solution",
    "maintainer": "Rowan Ember",
    "website": "zbye.odoo.com",
    "support": "zbye.info@gmail.com",
    "license": "LGPL-3",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/nrc_prefix_data.xml",
        "data/nrc_township_code_data.xml",
        "data/nrc_type_data.xml",
        "views/nrc_prefix_views.xml",
        "views/nrc_township_code_views.xml",
        "views/nrc_type_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["static/description/banner.png"],
}
