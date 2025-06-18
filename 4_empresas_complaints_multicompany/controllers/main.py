# -*- coding: utf-8 -*-

import logging
import werkzeug
import base64
from odoo import http, _
from odoo.exceptions import UserError
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
        """Get complaint form data for specific company"""
        try:
            domain = [('company_id', '=', company.id)]
            
            # Usar el contexto de la empresa específica
            env_with_company = request.env.sudo().with_context(
                allowed_company_ids=[company.id],
                force_company=company.id,
                active_test=False
            )
            
            return {
                'company': company,
                'reason_ids': env_with_company['complaint.complaint.reason'].search(domain),
                'categ_id': env_with_company['complaint.categ'].search(domain),
                'via_ids': env_with_company['complaint.via'].search(domain),
            }
        except Exception as e:
            _logger.error("Error getting complaint data for company %s: %s", company.id, str(e))
            return {
                'company': company,
                'reason_ids': request.env['complaint.complaint.reason'].sudo().browse([]),
                'categ_id': request.env['complaint.categ'].sudo().browse([]),
                'via_ids': request.env['complaint.via'].sudo().browse([]),
            }
        
    @http.route('/reclamo/<string:company_slug>', type='http', auth='public', website=True, sitemap=False)
    def company_complaint_form(self, company_slug, **kw):
        """Company-specific complaint form"""
        try:
            company = self._get_company_from_slug(company_slug)
            if not company:
                return request.render('website.404')

            values = request.params.copy()
            values.update(self._get_complaint_data(company))
            
            return request.render('4_empresas_complaints_multicompany.complaint_form', values)

        except Exception as e:
            _logger.error("Error rendering complaint form for slug '%s': %s", company_slug, str(e))
            return request.render('website.404')

    @http.route('/reclamo/<string:company_slug>/enviado', type='http', methods=['POST'], auth='public', website=True)
    def company_complaint_submit(self, company_slug, **kw):
        """Submit complaint for specific company"""
        company = self._get_company_from_slug(company_slug)
        if not company:
            return request.render('website.404')

        try:
            complaint_data = self._process_complaint_data(kw, company)
            complaint = request.env['complaint.complaint'].sudo().create(complaint_data)
            
            # Process reason_ids
            reason_arr = []
            for key, value in kw.items():
                if key.startswith('reason_') and key != 'reason_other' and value:
                    reason_arr.append(int(value))
            
            if reason_arr:
                complaint.reason_ids = [(6, 0, reason_arr)]

            values = {
                'company': company,
                'complaint': complaint,
                'success_message': company.complaint_success_message,
            }
            
            return request.render('4_empresas_complaints_multicompany.complaint_success', values)

        except Exception as e:
            _logger.error("Error creating complaint: %s", str(e))
            values = {
                'company': company,
                'error_message': _('An error occurred while processing your complaint. Please try again.'),
            }
            values.update(self._get_complaint_data(company))
            values.update(kw)  # Keep form data
            return request.render('4_empresas_complaints_multicompany.complaint_form', values)

    def _process_complaint_data(self, form_data, company):
        """Process and validate form data"""
        processed_data = {
            'company_id': company.id,
        }

        # Handle file upload
        if form_data.get('complaint_files'):
            file = form_data.get('complaint_files').read()
            processed_data['complaint_files'] = base64.b64encode(file)

        # Process form fields
        field_mapping = {
            'perspective': 'perspective',
            'date_incident': lambda x: x.replace('T', ' ') if x else None,
            'reason_other': 'reason_other',
            'solution': lambda x: bool(int(x)) if x else False,
            'name': 'complainer_name',
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

        # Handle category
        if form_data.get('categ_id'):
            categ_id = int(form_data['categ_id'])
            # Verify category belongs to company
            category = request.env['complaint.categ'].sudo().search([
                ('id', '=', categ_id),
                ('company_id', '=', company.id)
            ])
            if category:
                processed_data['categ_id'] = categ_id

        # Handle type
        if form_data.get('type'):
            type_mapping = {
                'Interna': 'customer',
                'Externa': 'supplier'
            }
            processed_data['type'] = type_mapping.get(form_data['type'])

        # Handle delivery type
        if form_data.get('complainer_delivery_type'):
            delivery_mapping = {
                'Quiero recibirla por correo electronico': 'email',
                'Quiero recibirla por celular': 'phone',
            }
            processed_data['complainer_delivery_type'] = delivery_mapping.get(form_data['complainer_delivery_type'])

        # Generate complaint name
        complaint_name = f"{form_data.get('name', 'Anónimo')} - {form_data.get('date_incident', '').replace('T', ' ')}"
        processed_data['name'] = complaint_name

        return processed_data

    @http.route('/reclamo', type='http', auth='public', website=True, sitemap=False)
    def complaint_redirect(self, **kw):
        """Redirect old complaint URL to default company or company selection"""
        # Try to get user's company or default company
        company = request.env.company
        if company and company.complaint_slug and company.complaint_form_active:
            return werkzeug.utils.redirect(f'/reclamo/{company.complaint_slug}')
        
        # Find any active company with complaint form
        active_company = request.env['res.company'].sudo().search([
            ('complaint_form_active', '=', True),
            ('complaint_slug', '!=', False)
        ], limit=1)
        
        if active_company:
            return werkzeug.utils.redirect(f'/reclamo/{active_company.complaint_slug}')
        
        # No active companies found
        return request.render('website.404')

    @http.route('/reclamos', type='http', auth='public', website=True, sitemap=True)
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