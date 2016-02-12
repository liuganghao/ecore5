# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.osv import fields, osv

class res_company_vat (osv.osv):
    _inherit = 'res.company'
    _columns = {
        'vat_check_vies': fields.boolean('VIES VAT Check',
                                         help="If checked, Partners VAT numbers will be fully validated against EU's VIES service "
                                              "rather than via a simple format validation (checksum)."),
    }

    
