{
    'name': '4 empresas HR Job Functions',
    'version': '1.0',
    'description': '4 empresas HR Job Functions, and employees',
    'summary': '4 empresas HR Job Functions',
    'author': 'Soy Calidad',
    'website': 'https://www.soycalidad.com',
    'license': 'Other proprietary',
    'category': 'Uncategorized',
    'depends': [
        'base', 
        'hr_job_functions',
        'mgmtsystem_employees',    
    ],
    'data': [
        'views/hr_job_function_views.xml',
        'views/plan_training_views.xml',
        'views/menus.xml',

        'reports/plan_training_line_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
