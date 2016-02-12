# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.osv import fields, osv
from ecore.tools.translate import _

class project_configuration(osv.osv_memory):
    _name = 'project.config.settings'
    _inherit = 'project.config.settings'

    _columns = {
        'group_tasks_work_on_tasks': fields.selection([
            (0, "Do not log work activities on task"),
            (1, "Log work activities on tasks")
            ], "Activity Log",
            implied_group='project.group_tasks_work_on_tasks',
            help="Allows you to compute work on tasks."),
    }