from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

from datetime import datetime
import tempfile
import base64


class JobProfile(models.Model):
    _inherit = 'hr.job.profile'

    degree = fields.Selection([
        ('none', 'Sin estudios'),
        ('elementary', 'Primaria completa'),
        ('high_school', 'Secundaria completa'),
        ('professional_training', 'Formación profesional'),
        ('college', 'Superior'),
        ('master', 'Maestría'),
        ('doctor', 'Doctorado')
    ])
    
    
