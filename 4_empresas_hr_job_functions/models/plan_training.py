from odoo import fields, api, models 

class PlanTraining(models.Model):
    _inherit = "mgmtsystem.plan.training"

    general_manager_id = fields.Many2one(
        comodel_name='hr.employee',
        string="Gerente general",
        help="El gerente general aparecera en el certificado de capacitación",
    )