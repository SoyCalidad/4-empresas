from odoo import fields, models 

class Review(models.Model):
    _inherit = "management.review"

    satisfaction_survey = fields.Text(string="Encuestas de satisfacción")