# -*- coding: utf-8 -*-
{
    'name': "العيادات",
    'version': '1.22',
    'category': 'Health',
'author': "أبوالعباس محمد خضر عجيب",
    'website': "https://ageebsoft.blogspot.com/",
    'summary': """
       22 نبذه مختصرة عن المشروع الطبي""",
    'sequence': 5,
    'description': """
       نبذه مطولة على المشروع الطبي   
       نبذه مطولة على المشروع الطبي
       نبذه مطولة على المشروع الطبي
    """,




    'images': [],
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/clinic_patient_view.xml',
        'views/clinic_doctor_view.xml',
        'views/DoctorSpecialty_views.xml',
        'views/clinic_booking_view.xml',

        # report
        'report/clinic_booking_report.xml',
        'report/clinic_booking_wiz_report.xml',
        'wizard/clinic_booking_wiz_view.xml',

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'css': ['static/src/css/.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',

}
