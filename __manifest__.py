# -*- coding: utf-8 -*-
{
    'name': "العيادات",

    'summary': """
       21 نبذه مختصرة عن المشروع الطبي""",

    'description': """
       نبذه مطولة على المشروع الطبي   
       نبذه مطولة على المشروع الطبي
       نبذه مطولة على المشروع الطبي
       نبذه مطولة على المشروع الطبي
       نبذه مطولة على المشروع الطبي
       نبذه مطولة على المشروع الطبي

    
    
    """,


    'author': "أبوالعباس محمد خضر عجيب",
    'website': "https://ageebsoft.blogspot.com/",

    'version': '1.1',
    'category': 'Health',
    'version': '0.1',
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

        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
