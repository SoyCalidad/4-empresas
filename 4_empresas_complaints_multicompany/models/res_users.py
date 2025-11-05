from odoo import api, models, fields 


class ResUsers(models.Model):
    _inherit = "res.users"
    
    report_incident = fields.Boolean(string="Recibir notificación del incidente", default=False,)