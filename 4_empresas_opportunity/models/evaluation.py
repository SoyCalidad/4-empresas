from odoo import api, fields, models


class Eval(models.Model):
    _inherit = 'evaluation.evaluation'

    criterio_ids = fields.One2many(copy=True)


class Criterio(models.Model):
    _inherit = 'evaluation.criterio'

    line_ids = fields.One2many(copy=True)
