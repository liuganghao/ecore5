# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'Employee Contracts',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Add all information on the employee form to manage contracts.
=============================================================

    * Contract
    * Place of Birth,
    * Medical Examination Date
    * Company Vehicle

You can assign several contracts per employee.
    """,
    'website': 'http://www.ecore.cool/page/employees',
    'depends': ['base_action_rule', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'hr_contract_view.xml',
        'hr_contract_data.xml',
        'base_action_rule_view.xml',
    ],
    'demo': [],
    'test': ['test/test_hr_contract.yml'],
    'installable': True,
    'auto_install': False,
}
