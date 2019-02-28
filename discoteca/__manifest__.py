# -*- coding: utf-8 -*-
{
    'name': "Discoteca",

    'summary': """
        Modulo para gestionar una discoteca""",

    'description': """
        Modulo diseñado para gestionar todos los empleados y clientes en una discoteca,
        ademas de actividades que se pueden realizar en esta.
    """,

    'author': "Roberto Ruiz",
    'website': "http://www.yourDiscoteca.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
