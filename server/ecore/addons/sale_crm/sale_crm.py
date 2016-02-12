# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.osv import osv, fields

class sale_order(osv.osv):
    _name = "sale.order"
    _inherit = ['sale.order', 'utm.mixin']
    _columns = {
        'tag_ids': fields.many2many('crm.lead.tag', 'sale_order_tag_rel', 'order_id', 'tag_id', 'Tags'),
        'opportunity_id': fields.many2one('crm.lead', 'Opportunity', domain="[('type', '=', 'opportunity')]")
    }
