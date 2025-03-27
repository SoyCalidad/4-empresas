{
    'name': '4 Empresas HR Organizational Chart',
    'version': '1.0',
    'description': '4 Empresas HR Organizational Chart',
    'summary': '4 Empresas HR Organizational Chart',
    'author': 'Soy Calidad',
    'website': 'https://www.soycalidad.com',
    'license': 'Other proprietary',
    'category': 'Uncategorized',
    'depends': ['base', 'hr_organizational_chart'],
    'data': [
        'views/show_employee_chart.xml',
        'views/assets.xml',
    ],
    'qweb': ['static/src/xml/chart_view.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
