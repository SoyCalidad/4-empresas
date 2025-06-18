# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResCompany(models.Model):
    _inherit = 'res.company'

    complaint_slug = fields.Char(
        string='Complaint URL Slug',
        help="URL slug for company-specific complaint form (e.g., 'company-a' for /reclamo/company-a)",
        required=False
    )
    
    complaint_form_active = fields.Boolean(
        string='Enable Complaint Form',
        default=True,
        help="Enable public complaint form for this company"
    )

    complaint_form_title = fields.Char(
        string='Complaint Form Title',
        default='Formulario de Reclamos',
        help="Title displayed on the complaint form"
    )

    complaint_form_subtitle = fields.Text(
        string='Complaint Form Subtitle',
        default='Complete el formulario para registrar su reclamo',
        help="Subtitle displayed on the complaint form"
    )

    complaint_success_message = fields.Html(
        string='Success Message',
        default='<h1>¡Gracias! Su reclamo ha sido enviado correctamente</h1>',
        help="Message displayed after successful complaint submission"
    )

    @api.constrains('complaint_slug')
    def _check_complaint_slug(self):
        """Validate complaint slug format and uniqueness"""
        for record in self:
            if record.complaint_slug:
                # Check format (letters, numbers, hyphens only)
                if not re.match(r'^[a-zA-Z0-9-]+$', record.complaint_slug):
                    raise ValidationError(_("Complaint slug can only contain letters, numbers, and hyphens."))
                
                # Check uniqueness
                existing = self.search([
                    ('id', '!=', record.id),
                    ('complaint_slug', '=', record.complaint_slug)
                ])
                if existing:
                    raise ValidationError(_("Complaint slug must be unique. '%s' is already used by %s.") % (record.complaint_slug, existing.name))

    @api.model
    def create(self, vals):
        """Auto-generate slug if not provided"""
        if not vals.get('complaint_slug') and vals.get('name'):
            vals['complaint_slug'] = self._generate_slug(vals['name'])
        return super(ResCompany, self).create(vals)

    def write(self, vals):
        """Auto-generate slug if name changes and slug is empty"""
        if vals.get('name') and not self.complaint_slug:
            vals['complaint_slug'] = self._generate_slug(vals['name'])
        return super(ResCompany, self).write(vals)

    def _generate_slug(self, name):
        """Generate URL-friendly slug from company name"""
        slug = name.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_-]+', '-', slug)
        slug = slug.strip('-')
        
        # Ensure uniqueness
        base_slug = slug
        counter = 1
        while self.search([('complaint_slug', '=', slug)]):
            slug = f"{base_slug}-{counter}"
            counter += 1
            
        return slug