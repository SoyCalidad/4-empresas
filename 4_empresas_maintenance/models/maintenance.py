from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    type_id = fields.Many2one('maintenance.equipment.type', string='Tipo')
    
    def unlink(self):
        if 'active' in self._fields:
            if self.active == True:
                self.write({'active': False})
                return True
        return super().unlink()
