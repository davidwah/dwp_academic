# -*- coding: utf-8 -*-
{
    'name': "Academic Course",
    'summary': """
        academic addons odoo""",
    'description': """
        Percobaan membuat addons odoo
    """,
    'author': "David Wahyu",
    'website': "http://dwp.my.id",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base'],
    'images': ['static\description\icon.png'],
    'data': [
        "menu.xml",
        "course.xml",
        "session.xml",
        "attendee.xml",
        "partner.xml"
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
}
