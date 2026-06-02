{
    'name': 'Payroll Auto Generate',
    'version': '15.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Automatically generate payroll for all employees based on schedule.',
    'description': """
        This module automates the generation of payroll for all employees of a company.
        It schedules payroll runs for a given month and computes payslips for all employees.
    """,
    'author': 'ZbyE Solution',
    
    'company': 'ZbyE Solution',
    
    'maintainer': 'Rowan Ember',
    
    'website': 'https://nexorionis.odoo.com',
    
    'email': 'zbye.info@gmail.com',
    
    'depends': ['hr','hr_payroll'],
    'data': [
            'data/scheduled_action.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}