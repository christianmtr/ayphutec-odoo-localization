# -*- coding: utf-8 -*-
{
    'name': "AyphuTec Localization",

    'summary': """
        Módulo contable y RR. HH. de AyphuTec para Perú.""",

    'description': """
        Módulo contable y RR. HH. de AyphuTec para Perú, todo listo para trabajar con SUNAT.
    """,

    'author': "Ayphu Tec SAC.",
    'website': "https://ayphutec.com/",
    'application': 'true',
    'installable': 'true',
    # 'auto_install': 'true',  # fails in odoo.sh
    'maintainer': 'Christian M.',
    'license': 'Other proprietary',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'module_category_localization',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant', 'hr', 'l10n_pe',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/trees.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
