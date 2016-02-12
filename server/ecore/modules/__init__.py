# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

""" Modules (also called addons) management.

"""

from . import db, graph, loading, migration, module, registry

from ecore.modules.loading import load_modules

from ecore.modules.module import get_modules, get_modules_with_version, \
    load_information_from_description_file, get_module_resource, get_module_path, \
    initialize_sys_path, load_ecore_module, init_module_models, adapt_version, \
    get_resource_path, get_resource_from_path
