{
    'name': 'Spare Part Management',
    'version': '15.0.1.0.0',
    'summary': 'Manage spare parts of products in Odoo 15',
    'description': 'This module allows managing spare parts for products, tracking stock, and linking child components to parent products.',
    "depends":
        [
            "stock",
            "stock_account",
        ],
    "data": [
        'security/ir.model.access.csv',
        'data/tempory_location.xml',
        'views/spare_part_stock_view.xml',
        'wizards/spare_part_confirm_wizard.xml',
    ],
    'author': 'ZbyE Solution',
    
    'company': 'ZbyE Solution',
    
    'maintainer': 'Rowan Ember',

    'email': 'zbye.info@gmail.com',
    
    'website': 'https://nexorionis.odoo.com',
    'license': 'LGPL-3',
    "installable": True,
    "application": True,
    "auto_install": False,

    'images': ['static/description/banner.jpg'],
}
