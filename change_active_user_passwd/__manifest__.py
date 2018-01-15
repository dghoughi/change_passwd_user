# -*- coding: utf-8 -*-
{
    'name': "change active user password",

    'summary': """
        this module allow any user to update his personal password without having Access Rights .
        """,

    'description': """
       this module allow any user to update his personal password without having Access Rights .
       
        this is my first module in odoo apps please if any one find it useful 
        or any ideas to add please let me know by email  'dghoughi2403@gmail.com' 
        this will encorage me to make more 
    """,

    'author': "Marocsys",
    'website': "http://www.marocsys.com",

    'category': 'Tools',
    'version': '10.0',

    'depends': ['base'],

    'data': [
        'security/change_passwd_security.xml',
        'views/change_passwd.xml',
    ],
    'images' : ['static/images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}