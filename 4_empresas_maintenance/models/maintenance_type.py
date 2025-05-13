from odoo import fields, models


class MaintenanceEquipmentType(models.Model):
    _name = 'maintenance.equipment.type'
    _order = 'sequence, name'

    name = fields.Char(string='Nombre')
    sequence = fields.Integer(string='Secuencia', default=10)
    active = fields.Boolean(string='Activo', default=True)
