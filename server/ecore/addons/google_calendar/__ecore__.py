# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'Google Calendar',
    'version': '1.0',
    'category': 'Tools',
    'description': """
The module adds the possibility to synchronize Google Calendar with eCore
===========================================================================
""",
    'website': 'http://www.ecore.cool/page/crm',
    'depends': ['google_account', 'calendar'],
    'qweb': ['static/src/xml/*.xml'],
    'data': [
        'res_config_view.xml',
        'security/ir.model.access.csv',
        'views/google_calendar.xml',
        'views/res_users.xml',
        'google_calendar.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
