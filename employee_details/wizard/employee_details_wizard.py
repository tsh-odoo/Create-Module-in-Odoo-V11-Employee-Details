from odoo import models, fields, api

class EmployeeProjectWizard(models.TransientModel):
    _name = 'employee.projects.wizard'

    employee_id = fields.Many2one('employee.details',
        string="Employee", required=True)
    languages = fields.Many2many('languages', string="Languages")