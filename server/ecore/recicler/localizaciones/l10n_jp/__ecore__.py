# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

# Copyright (C) Rooms For (Hong Kong) Limited T/A OSCG

{
    'name': 'Japan - Accounting',
    'version': '1.2',
    'category': 'Localization/Account Charts',
    'description': """

Overview:
---------

* Chart of Accounts and Taxes template for companies in Japan.
* This probably does not cover all the necessary accounts for a company. \
You are expected to add/delete/modify accounts based on this template.

Note:
-----

* Fiscal positions '内税' and '外税' have been added to handle special \
requirements which might arise from POS implementation. [1]  You may not \
need to use these at all under normal circumstances.

[1] See https://github.com/ecore/ecore/pull/6470 for detail.

    """,
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG',
    'website': 'http://www.ecore-asia.net/',
    'depends': ['account'],
    'data': [
        'data/account_chart_template.xml',
        'data/account.account.template.csv',
        'data/account.tax.template.csv',
        'data/account_chart_template_after.xml',
        'data/account_chart_template.yml',
        'data/account.fiscal.position.template.csv',
    ],
    'installable': True,
}
