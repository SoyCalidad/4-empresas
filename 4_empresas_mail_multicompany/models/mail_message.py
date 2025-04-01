from odoo import api, fields, models
from email.header import Header
from email.utils import formataddr
import re


class MailMessage(models.Model):
    _inherit = "mail.message"

    company_id = fields.Many2one("res.company", "Company")

    @api.model_create_multi
    def create(self, values_list):
        for vals in values_list:
            if vals.get("model") and vals.get("res_id"):
                current_object = self.env[vals["model"]].browse(vals["res_id"])
                if hasattr(current_object, "company_id") and current_object.company_id:
                    vals["company_id"] = current_object.company_id.id

            if not vals.get("company_id"):
                vals["company_id"] = self.env.company.id

            if not vals.get("mail_server_id"):
                mail_server = self.sudo().env["ir.mail_server"].search(
                    [("company_id", "=", vals.get("company_id", False))],
                    order="sequence",
                    limit=1,
                )
                vals["mail_server_id"] = mail_server.id
                if mail_server and mail_server.smtp_user:
                    if vals.get("email_from"):
                        vals["reply_to"] = vals["email_from"]

                    company_name = self.sudo().env["res.company"].browse(vals["company_id"]).name

                    def is_valid_email(email):
                        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

                    if is_valid_email(mail_server.smtp_user):
                        company_name_encoded = str(Header(company_name, 'utf-8'))
                        formatted_email_from = formataddr((company_name_encoded, mail_server.smtp_user))
                        vals["email_from"] = formatted_email_from
                    else:
                        vals["email_from"] = "no-reply@example.com"

        return super(MailMessage, self).create(values_list)
