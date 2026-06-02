# -*- coding: utf-8 -*-
{
    'name': "Customer Scanner",
    'summary': "Scanner for Member Customers in POS",
    'description': """
Customer Scanner for POS
========================

This module extends the Point of Sale (POS) functionality to allow scanning 
of customer barcodes or QR codes directly at the POS interface.

Key Features:
-------------
- If the scanned barcode matches a **product**, the product will be added to the order as usual.  
- If the scanned barcode does **not** match any product, the system will then search among **customers (partners)**.  
- When a matching customer is found, that customer is automatically set as the order’s customer in POS.  
- Supports both **barcode** and **QR code** scanning for customers.  

Use Case:
---------
Ideal for businesses with membership cards or loyalty programs where each 
customer is assigned a unique barcode/QR code for quick identification 
during checkout.
    """,

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
    'category': 'POS',
    'version': '1.0',
    'depends': [
        'point_of_sale',
        'base',
    ],
    'data': [],
    'assets': {
        'point_of_sale.assets': [
            'noi_pos_customer_scanner/static/src/js/Screens/ProductScreens/*',
        ],
        'web.assets_qweb': [
        ],
    },
}
