# -*- coding: utf-8 -*-
{
    'name': "Time Picker Field",

    'summary': """Time Picker Using Wickedpicker""",

    'author': "Mounir Lahsini",
    'website': "https://github.com/matteopolleschi/field_timepicker",

    'category': 'Tools',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'views/templates.xml',
    ],

    'qweb': [
        'static/src/xml/timepicker.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
}