# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

{
    'name': 'Google Drive™ integration',
    'version': '0.2',
    'category': 'Tools',
    'installable': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'res_config_user_view.xml',
        'google_drive_data.xml',
        'views/google_drive.xml',
    ],
    'demo': [
        'google_drive_demo.xml'
    ],
    'depends': ['base_setup', 'google_account'],
    'description': """
Integrate google document to eCore record.
============================================

This module allows you to integrate google documents to any of your eCore record quickly and easily using OAuth 2.0 for Installed Applications,
You can configure your google Authorization Code from Settings > Configuration > General Settings by clicking on "Generate Google Authorization Code"
"""
}
