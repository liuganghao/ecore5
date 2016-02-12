# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

import ir
import workflow
import module
import res
import report
import tests

def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from ecore import SUPERUSER_ID
    from ecore.addons.base.ir.ir_config_parameter import _default_parameters
    ICP = registry['ir.config_parameter']
    for k, func in _default_parameters.items():
        v = ICP.get_param(cr, SUPERUSER_ID, k)
        _, g = func()
        ICP.set_param(cr, SUPERUSER_ID, k, v, g)
