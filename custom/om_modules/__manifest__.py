{
    'name': "Hospital Management System",
    'version': '12.0.1.0.0',
    'depends': ['base'],
    'author': "Sathir Plus, Codeso LK",
    'license':"AGPL-3",
    'category': 'Extra Tools',
    'description': """
    Modules for Managing the Hospitals
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'patient.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}