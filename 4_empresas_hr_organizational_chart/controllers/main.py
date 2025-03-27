from odoo import http
from odoo.exceptions import UserError
from odoo.http import request
from odoo.addons.hr_organizational_chart.controller.main import EmployeeChart


class EmployeeChart(EmployeeChart):

    @http.route('/get/parent/employee', type='json', auth='public', methods=['POST'], csrf=False)
    def get_employee_ids(self, **kwargs):
        company_id = kwargs.get('company_id', False)
        domain = [('parent_id', '=', False)]
        if company_id:
            domain.append(('company_id', '=', company_id))
        employees = request.env['hr.employee'].sudo().search(domain)
        names = []
        key = []

        if len(employees) == 1:
            key.append(employees.id)
            key.append(len(employees.child_ids))
            return key

        elif len(employees) == 0:
            raise UserError(
                "No top-level manager found for the employee in the chart.")
        else:
            for emp in employees:
                names.append(emp.name)
            raise UserError("These employees have no manager: %s" % (names))
