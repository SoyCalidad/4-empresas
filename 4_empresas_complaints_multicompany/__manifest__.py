{
    'name': '4empresas Complaints',
    'version': '1.0',
    'description': '4empresas Complaints',
    'summary': '4empresas Complaints',
    'author': 'Soy Calidad',
    'website': 'https://www.soycalidad.com',
    'license': 'Other proprietary',
    'category': 'Uncategorized',
    'depends': [
        'mgmtsystem_complaints',
        'website',
        'base',
    ],
    'data': [
        'security/security_rules.xml',
        'security/update_rules.xml',
        'views/complaint_views.xml',
        'views/res_company.xml',
        'templates/complaint_templates.xml',
        'views/config_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            #'4_empresas_complaints_multicompany/static/src/css/complaint.css',
            #'4_empresas_complaints_multicompany/static/src/js/complaint.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
