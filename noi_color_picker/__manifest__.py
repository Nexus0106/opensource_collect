# -*- coding: utf-8 -*-
{
    "name": "Color Picker Widget",
    "version": "17.0.1.0.0",
    "summary": "Color Picker Widget for Char Fields",
    "description": """
        A simple color picker widget that can be used with Char fields.
        Usage: <field name="your_field" widget="noi_color_picker"/>
        The selected color will be stored as a HEX value (e.g., #FF5733).
    """,
    'category': 'Tools',
    'author': 'ZbyE Solution',
    'company': 'ZbyE Solution',
    'maintainer': 'Rowan Ember',
    'website': 'zbye.odoo.com',
    "support": "zbye.info@gmail.com",
    'depends': [
        "web"
    ],
    "license": "LGPL-3" ,
    'data': [
    ],
    "assets": {
        "web.assets_backend": [
            "noi_color_picker/static/src/js/color_picker_field.js",
            "noi_color_picker/static/src/js/color_picker_field.xml",
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}