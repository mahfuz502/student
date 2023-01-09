# -*- coding: utf-8 -*-
{
    'name': 'odoo_tutorial_backend',
    'summary': """
    short  (1phrase/line) summary of the module's purpose, used as
    subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
        """,
    'author': "MY Company",
    'website': "http:/www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base',
                'web'],
    'data': [
        'views/views.xml',
        'views/menus.xml',
    ],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': '',
    'license': '',
    'contributors': [
    ],
}


