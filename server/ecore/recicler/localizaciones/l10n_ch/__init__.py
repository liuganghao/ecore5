# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

# Author: Nicolas Bessi. Copyright Camptocamp SA
# Financial contributors: Hasa SA, Open Net SA,
#                         Prisme Solutions Informatique SA, Quod SA
# Translation contributors: brain-tec AG, Agile Business Group

from ecore import SUPERUSER_ID

def load_translations(cr, registry):
    chart_template = registry['ir.model.data'].xmlid_to_object(cr, SUPERUSER_ID, 'l10n_ch.l10nch_chart_template')
    chart_template.process_coa_translations()