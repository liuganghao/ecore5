# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'MRP Byproducts',
    'version': '1.0',
    'category': 'Manufacturing',
    'description': """
This module allows you to produce several products from one production order.
=============================================================================

You can configure by-products in the bill of material.

Without this module:
--------------------
    A + B + C -> D

With this module:
-----------------
    A + B + C -> D + E
    """,
    'website': 'http://www.ecore.cool/page/manufacturing',
    'depends': ['base', 'mrp'],
    'data': [
       'security/ir.model.access.csv',
       'mrp_byproduct_view.xml'
    ],
    'demo': [],
    'test': ['test/mrp_byproduct.yml'],
    'installable': True,
    'auto_install': False,
}
