from odoo import models 

import logging 

_logger = logging.getLogger(__name__)
class Validation(models.Model):
    _inherit = 'mgmtsystem.validation'
    
    def notify_to_step_users(self, steps, type):
        #override
        body = ''
        self.env.cr.execute("""SELECT id FROM ir_model 
                            WHERE model = %s""", (str(self._name),))
        info = self.env.cr.dictfetchall()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')

        # Construir URL al formulario del registro
        record_url = f"{base_url}/web#id={self.id}&model={self._name}&view_type=form"
        if info:
            model_id = info[0]['id']
        if type == 'elaboration':
            body += 'Elaboración de documento'
        elif type == 'review':
            body += 'Revisión de documento'
        elif type == 'validation':
            body += 'Validación de documento'
        for step in steps:
            name = self.name or ''
            if step.user_id:
                todo_id = self.env['mail.activity.type'].search(
                    [('name', '=', 'To Do')], limit=1).id
                self.env['mail.activity'].create({
                    'res_id': self.ids[0],
                    'res_model_id': model_id,
                    'res_model': self._name,
                    'summary': body,
                    'user_id': step.user_id.id,
                    'activity_type_id': int(todo_id),
                })
                if not step.user_id or not step.user_id.partner_id.email:
                    continue

                mail_values = {
                    'subject': body,
                    'body_html': f"""
                        <p>{body}</p>
                        <p>Documento: {name}</p>
                        <p>
                            Puede revisar el documento aquí:<br/>
                            <a href="{record_url}">Ver Documento</a>
                        </p>
                    """,
                    'email_to': step.user_id.partner_id.email,
                }

                mail = self.env['mail.mail'].create(mail_values)
                mail.send()