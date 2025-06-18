# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ComplaintComplaint(models.Model):
    _inherit = 'complaint.complaint'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        default=lambda self: self.env.company,
        help="Company that owns this complaint"
    )

    @api.model
    def create(self, vals):
        # Ensure company_id is set if not provided
        if not vals.get('company_id'):
            vals['company_id'] = self.env.company.id
        return super(ComplaintComplaint, self).create(vals)

    @api.constrains('company_id')
    def _check_company_consistency(self):
        """Ensure related records belong to the same company"""
        for record in self:
            if record.partner_id and record.partner_id.company_id and record.partner_id.company_id != record.company_id:
                raise ValidationError(_("The partner's company must match the complaint's company."))
            if record.department_id and record.department_id.company_id and record.department_id.company_id != record.company_id:
                raise ValidationError(_("The department's company must match the complaint's company."))


class ComplaintCateg(models.Model):
    _inherit = 'complaint.categ'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        #default=lambda self: self.env.company,
        help="Company that owns this category"
    )


class ComplaintVia(models.Model):
    _inherit = 'complaint.via'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        #default=lambda self: self.env.company,
        help="Company that owns this via"
    )


class ComplaintQuickAction(models.Model):
    _inherit = 'complaint.quick.action'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        #default=lambda self: self.env.company,
        help="Company that owns this quick action"
    )

    @api.onchange('categ_id')
    def _onchange_categ_id_company(self):
        """Filter categories by company"""
        if self.company_id:
            return {'domain': {'categ_id': [('company_id', '=', self.company_id.id)]}}


class ComplaintComplaintReason(models.Model):
    _inherit = 'complaint.complaint.reason'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        #default=lambda self: self.env.company,
        help="Company that owns this reason"
    )


class ComplaintAnalisis(models.Model):
    _inherit = 'complaint.analisis'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=False,
        #default=lambda self: self.env.company,
        help="Company that owns this analysis"
    )
