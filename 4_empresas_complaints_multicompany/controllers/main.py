# -*- coding: utf-8 -*-

import logging
import werkzeug
import base64
from odoo import http, _
from odoo.exceptions import UserError
from odoo import SUPERUSER_ID
from odoo.http import request
from odoo.addons.website.controllers.main import Website

_logger = logging.getLogger(__name__)


class ComplaintMultiCompany(http.Controller):


    def _get_company_from_slug(self, company_slug):
        """Get company by slug, return None if not found or not active"""
        try:
            # Busca la empresa sin restricciones de multi-company
            company = request.env['res.company'].sudo().with_context(
                active_test=False,
                force_company=False,
                allowed_company_ids=[]
            ).search([
                ('complaint_slug', '=', company_slug),
                ('complaint_form_active', '=', True)
            ], limit=1)
            
            return company if company else None
        except Exception as e:
            _logger.error("Error getting company from slug '%s': %s", company_slug, str(e))
            return None


    def _get_complaint_data(self, company):
        dom = ['|',
            ('company_id', '=', company.id),
            ('company_id', '=', False),
        ]

        # Recordset sudo y contexto multi-empresa
        env_ctx = request.env['complaint.categ'].sudo().with_context(
            force_company       = company.id,
            allowed_company_ids = [company.id],
            active_test         = False,
        ).env                                     # ← recuperamos el Environment

        categs  = [(c.id,  c.name) for c in env_ctx['complaint.categ'].search(dom)]
        reasons = [
            (r.id, r.name, (r.description or ''))      # ← 3-element tuple
            for r in env_ctx['incident.incident.reason'].search([])
        ]
        vias    = [(v.id, v.name)  for v in env_ctx['complaint.via'].search(dom)]

        return {
            'company'   : company,
            'categs'    : categs,
            'categ_id'  : request.params.get('categ_id'),
            'reason_ids': reasons,
            'via_ids'   : vias,
        }


    @http.route('/incidente/<string:company_slug>', type='http', auth='public', website=True, sitemap=False)
    def company_complaint_form(self, company_slug, **kw):
        """Company-specific complaint form"""
        try:
            company = self._get_company_from_slug(company_slug)
            if not company:
                return request.render('website.404')

            values = request.params.copy()
            values.update(self._get_complaint_data(company))
            
            _logger.info("DEBUG reasons = %s", values['reason_ids'][:5])  # ← añade esto

            return request.render('4_empresas_complaints_multicompany.complaint_form', values)

        except Exception as e:
            _logger.error("Error rendering complaint form for slug '%s': %s", company_slug, str(e))
            return request.render('website.404')

    @http.route('/incidente/<string:company_slug>/enviado', type='http', methods=['POST'], auth='public', website=True)
    def company_complaint_submit(self, company_slug, **kw):
        """Submit complaint for specific company"""
        company = self._get_company_from_slug(company_slug)
        if not company:
            return request.render('website.404')

        try:
            real_values = self._process_complaint_data(kw, company)
            incidentModel = request.env['incident.incident']
            
            reason_arr = []

            for val in kw.keys():
                if val=='complainer_delivery_type' or val=='incident_files':
                    continue
                if kw[val]:
                    if val == 'date_incident':
                        real_values[val] = kw[val].replace('T', ' ')
                    elif val == 'reason_other':
                        real_values[val] = kw[val]
                    elif 'reason_' in val:
                        reason_arr.append(kw[val])
                    elif val == 'type':
                        if kw[val] == 'Interna':
                            real_values[val] = 'internal'
                        elif kw[val] == 'Externa':
                            real_values[val] = 'ext'
                        if kw.get('type') and kw['type'] == 'Externa':
                            partner_id = request.env['res.partner'].sudo().search(
                                [('name', '=', kw[val])])
                            if partner_id:
                                real_values['partner_id'] = partner_id.id
                        elif kw.get('type') and kw['type'] == 'Interna':
                            employee_id = request.env['hr.employee'].sudo().search(
                                [('name', '=', kw[val])])
                            if employee_id:
                                real_values['employee_notify_id'] = employee_id.id

                    else:
                        real_values[val] = kw[val]
                    
            real_values['complainer_name'] = kw['name']
            res_id = incidentModel.sudo().create(real_values)
            res_id.reason_ids = [(6, 0, reason_arr)]
            
            self._send_email_notify(res_id.id, res_id._name, [res_id.company_id.id])
            values = {
                'company': company,
                'complaint': res_id,
                'success_message': company.complaint_success_message,
            }
            
            #return request.render('4_empresas_complaints_multicompany.complaint_success', values)
            return request.render('soy_cybersecurity_cybersecurity.incident_done', {})

        except Exception as e:
            _logger.error("Error creating complaint: %s", str(e))

            request.env.cr.rollback()          # ← limpia la transacción

            values = {
                'company': company,
                'error_message': _('An error occurred while processing your complaint. Please try again.'),
            }
            values.update(self._get_complaint_data(company))
            values.update(kw)  # Keep form data
            return request.render('4_empresas_complaints_multicompany.complaint_form', values)
        
    def _send_email_notify(self, record_id, model_name, company_ids):
        _logger.info("init send email")
        group = request.env.ref('soy_cybersecurity_cybersecurity.group_cybersecurity_write_printreport').sudo()
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        record_url = f"{base_url}/web#id={record_id}&model={model_name}&view_type=form"

        _logger.info("Init group ")
        if group:
            users = group.users.sudo().search([('company_ids', 'in', company_ids)])
        else:
            users = []
            
        _logger.info(f"users email: {users}")
        for user in users:
            mail_values = {
                    "subject": f"Tiene un incidente por revisar",
                    "body_html": f"<p>Hola {user.display_name},</p><p>Tiene un incidente por revisar</p> <p>Puedes verlo aquí: <a href={record_url}>Ver registro</a></p>",
                    "email_to": user.email,
                }
            request.env["mail.mail"].sudo().create(mail_values).send()
    

    def _process_complaint_data(self, form_data, company):
        """Process and validate form data"""
        processed_data = {
            'company_id': company.id,
        }

        # Handle file upload
        if form_data.get('incident_files'):
            file = form_data.get('incident_files').read()
            processed_data['incident_files'] = base64.b64encode(file)

        # Process form fields
        field_mapping = {
            'perspective': 'perspective',
            'date_incident': lambda x: x.replace('T', ' ') if x else None,
            'reason_other': 'reason_other',
            #'solution': lambda x: bool(int(x)) if x else False,
            #'name': 'complainer_name',
            'complainer_document_number': 'complainer_document_number',
            'complainer_phone': 'complainer_phone',
            'complainer_email': 'complainer_email',
        }

        for form_field, db_field in field_mapping.items():
            if form_data.get(form_field):
                if callable(db_field):
                    processed_data[form_field] = db_field(form_data[form_field])
                else:
                    processed_data[db_field] = form_data[form_field]


        # Handle delivery type
        if form_data.get('complainer_delivery_type'):
            delivery_mapping = {
                'Quiero recibirla por correo electronico': 'email',
                'Quiero recibirla por celular': 'phone',
            }
            processed_data['complainer_delivery_type'] = delivery_mapping.get(form_data['complainer_delivery_type'])

        # Generate complaint name
        complaint_name = f"{form_data.get('name', 'Anónimo')}  {form_data.get('date_incident', '').replace('T', ' ')}"
        processed_data['name'] = complaint_name or '-'

        return processed_data

    @http.route('/incidente', type='http', auth='public', website=True, sitemap=False)
    def complaint_redirect(self, **kw):
        """Redirect old complaint URL to default company or company selection"""
        # Try to get user's company or default company
        company = request.env.company
        if company and company.complaint_slug and company.complaint_form_active:
            return werkzeug.utils.redirect(f'/incidente/{company.complaint_slug}')
        
        # Find any active company with complaint form
        active_company = request.env['res.company'].sudo().search([
            ('complaint_form_active', '=', True),
            ('complaint_slug', '!=', False)
        ], limit=1)
        
        if active_company:
            return werkzeug.utils.redirect(f'/incidente/{active_company.complaint_slug}')
        
        # No active companies found
        return request.render('website.404')

    @http.route('/incidentes', type='http', auth='public', website=True, sitemap=True)
    def company_complaint_list(self, **kw):
        """List available complaint forms by company"""
        companies = request.env['res.company'].sudo().search([
            ('complaint_form_active', '=', True),
            ('complaint_slug', '!=', False)
        ])
        
        values = {
            'companies': companies,
        }
        
        return request.render('4_empresas_complaints_multicompany.company_list', values)