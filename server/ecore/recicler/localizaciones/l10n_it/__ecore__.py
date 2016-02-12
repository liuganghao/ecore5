# -*- encoding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

{
    'name': 'Italy - Accounting',
    'version': '0.2',
    'depends': ['base_vat','base_iban'],
    'author': 'eCore Italian Community',
    'description': """
Piano dei conti italiano di un'impresa generica.
================================================

Italian accounting chart and localization.
    """,
    'category': 'Localization/Account Charts',
    'website': 'http://www.ecore-italia.org/',
    'data': [
        'data/account_chart.xml',
        'data/account.account.template.csv',
        'data/account.tax.template.csv',
        'data/account.fiscal.position.template.csv',
        'data/account.chart.template.csv',
        'data/account_chart_template.yml',
        ],
    'demo': [],
    'auto_install': False,
    'installable': True,
}
