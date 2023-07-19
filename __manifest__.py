# BY : Omar elkazini
# Visite https://github.com/casinoomarelkazini/School_manager for more information
{
    'name': 'School',
    'version': '13.0.0.0.1',
    'summary': 'Record Student Information',
    'description': '',
    'category': 'Tools',
    'author': 'omar elkazini',
    'maintainer': "",
    'company': '',
    'website': 'https://github.com/casinoomarelkazini/School_manager',
    'license': 'AGPL-3',
    'depends': ['base', 'mail', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/student_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}

