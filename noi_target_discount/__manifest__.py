{
    'name': 'Target Discount Configuration',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Global discount based on customer historical invoice totals',
    'description': """
        Configure target discount slabs based on customer's historical posted invoice totals.
        - Yearly or monthly period configuration
        - Automatic discount calculation on sales orders
        - Discount flows to invoice with proper accounting
    """,
    "author": "ZbyE Solution",
    "maintainer": "ZbyE Solution",
    "website": "nexorionis.odoo.com",
    "support": "zbye.info@gmail.com",
    "images": ["static/description/banner.jpg"],
    'license': 'LGPL-3',
    'depends': ['sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'data/product_data.xml',
        'views/target_discount_config_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
