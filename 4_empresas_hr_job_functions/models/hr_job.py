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
    
    
class HrJob(models.Model):
    _inherit = "hr.job"
    
    def notify_employee_email(self):
        super().notify_employee_email()
        total_empleados = len(self.employee_ids)
        if total_empleados>0:
            sender = self.env.company.email
            date = datetime.now().strftime('%d/%m/%Y')
            body = f'Usted ha realizado la acción de comunicar MOF del puesto {self.name}. Actualmente, este documento ha sido comunicado a {total_empleados} empleados. Se adjunta el MOF'
            fp = tempfile.NamedTemporaryFile(suffix='.pdf')
            data, data_format = self.env.ref('hr_job_functions.report_funinings').render([self.id])
            fp.write(data)
            part = open(fp.name, 'rb').read()
            attachment = self.env['ir.attachment'].create({
                'datas': base64.b64encode(part),
                'name': 'Manual de organización y funciones.pdf'})
            template_data = {
                'subject': "Comunicación del MOF %s" % date,
                'body_html': body,
                'email_from': sender,
                'email_to': self.env.user.email_normalized,
                'attachment_ids': [(4, attachment.id)]
            }
            self.env['mail.mail'].create(template_data).send()

            self.message_post(
                body="Se comunico el MOF con éxito.",
                message_type='comment',
                subtype_xmlid='mail.mt_comment'
            )
