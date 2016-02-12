# -*- coding: utf-8 -*-
{
    'name': 'Website Live Support',
    'category': 'Website',
    'summary': 'Chat With Your Website Visitors',
    'version': '1.0',
    'description': """
eCore Website LiveChat
========================
For website built with eCore CMS, this module include a chat button on your Website, and allow your visitors to chat with your collabarators.
It also will include the feedback tool for the livechat, and web pages to display your channel and its ratings on the website.
        """,
    'depends': ['website', 'im_livechat'],
    'installable': True,
    'data': [
        'views/website_livechat.xml',
        'views/res_config.xml',
        'views/website_livechat_view.xml',
        'security/ir.model.access.csv',
        'security/website_livechat.xml',
        'website_livechat_data.xml',
    ],
}
