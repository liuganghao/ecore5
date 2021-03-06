# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.tests import common


class test_challenge(common.TransactionCase):

    def setUp(self):
        super(test_challenge, self).setUp()
        cr, uid = self.cr, self.uid
        self.data_obj = self.registry('ir.model.data')
        self.user_obj = self.registry('res.users')

        self.challenge_obj = self.registry('gamification.challenge')
        self.line_obj = self.registry('gamification.challenge.line')
        self.goal_obj = self.registry('gamification.goal')
        self.badge_obj = self.registry('gamification.badge')
        self.badge_user_obj = self.registry('gamification.badge.user')

        self.demo_user_id = self.data_obj.get_object_reference(cr, uid, 'base', 'user_demo')[1]
        self.group_user_id = self.data_obj.get_object_reference(cr, uid, 'base', 'group_user')[1]
        self.challenge_base_id = self.data_obj.get_object_reference(cr, uid, 'gamification', 'challenge_base_discover')[1]
        self.definition_timezone_id = self.data_obj.get_object_reference(cr, uid, 'gamification', 'definition_base_timezone')[1]
        self.badge_id = self.data_obj.get_object_reference(cr, uid, 'gamification', 'badge_good_job')[1]

    def test_00_join_challenge(self):
        cr, uid, context = self.cr, self.uid, {}

        user_ids = self.user_obj.search(cr, uid, [('groups_id', '=', self.group_user_id)])
        challenge = self.challenge_obj.browse(cr, uid, self.challenge_base_id, context=context)

        self.assertGreaterEqual(len(challenge.user_ids), len(user_ids), "Not enough users in base challenge")

        self.user_obj.create(cr, uid, {
            'name': 'R2D2',
            'login': 'r2d2@ecore.cool',
            'email': 'r2d2@ecore.cool',
            'groups_id': [(6, 0, [self.group_user_id])]
        }, {'no_reset_password': True})

        self.challenge_obj._update_all(cr, uid, [self.challenge_base_id], context=context)
        challenge = self.challenge_obj.browse(cr, uid, self.challenge_base_id, context=context)
        self.assertGreaterEqual(len(challenge.user_ids), len(user_ids)+1, "These are not droids you are looking for")

    def test_10_reach_challenge(self):
        cr, uid, context = self.cr, self.uid, {}
        
        self.challenge_obj.write(cr, uid, [self.challenge_base_id], {'state': 'inprogress'}, context=context)
        challenge = self.challenge_obj.browse(cr, uid, self.challenge_base_id, context=context)
        challenge_user_ids = [user.id for user in challenge.user_ids]

        self.assertEqual(challenge.state, 'inprogress', "Challenge failed the change of state")

        line_ids = self.line_obj.search(cr, uid, [('challenge_id', '=', self.challenge_base_id)], context=context)
        goal_ids = self.goal_obj.search(cr, uid, [('challenge_id', '=', self.challenge_base_id), ('state', '!=', 'draft')], context=context)
        self.assertEqual(len(goal_ids), len(line_ids)*len(challenge_user_ids), "Incorrect number of goals generated, should be 1 goal per user, per challenge line")

        # demo user will set a timezone
        self.user_obj.write(cr, uid, self.demo_user_id, {'tz': "Europe/Brussels"}, context=context)
        goal_ids = self.goal_obj.search(cr, uid, [('user_id', '=', self.demo_user_id), ('definition_id', '=', self.definition_timezone_id)], context=context)
        
        self.goal_obj.update(cr, uid, goal_ids, context=context)
        reached_goal_ids = self.goal_obj.search(cr, uid, [('id', 'in', goal_ids), ('state', '=', 'reached')], context=context)
        self.assertEqual(set(goal_ids), set(reached_goal_ids), "Not every goal was reached after changing timezone")

        # reward for two firsts as admin may have timezone
        self.challenge_obj.write(cr, uid, self.challenge_base_id, {'reward_first_id': self.badge_id, 'reward_second_id': self.badge_id}, context=context)
        self.challenge_obj.write(cr, uid, self.challenge_base_id,  {'state': 'done'}, context=context)

        badge_ids = self.badge_user_obj.search(cr, uid, [('badge_id', '=', self.badge_id), ('user_id', '=', self.demo_user_id)])
        self.assertGreater(len(badge_ids), 0, "Demo user has not received the badge")