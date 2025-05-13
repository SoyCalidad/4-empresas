from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    type_id = fields.Many2one('maintenance.equipment.type', string='Tipo')
