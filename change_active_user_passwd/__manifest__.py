# -*- coding: utf-8 -*-
{
    'name': "change active user passwd",

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

    'category': 'Human Resources',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/change_passwd_security.xml',
        'views/change_passwd.xml',
    ],
    'application': True,
}