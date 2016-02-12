# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2010 Savoir-faire Linux (<https://www.savoirfairelinux.com>).
from ecore import SUPERUSER_ID

def load_translations(cr, registry):
    chart_template = registry['ir.model.data'].xmlid_to_object(cr, SUPERUSER_ID, 'l10n_ca.ca_en_chart_template_en')
    chart_template.process_coa_translations()
