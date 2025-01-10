from odoo import models, fields, api
from datetime import datetime, timedelta

class PayrollAutoGenerate(models.Model):
    _name = 'payroll.auto.generate'
    _description = 'Automatic Payroll Generator'

    @api.model
    def auto_generate_payroll(self):
        """Automatically generate and compute payroll for all employees."""
        # Get the current date
        today = datetime.now()
        # Determine the payroll period (last month)
        start_date = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        end_date = today.replace(day=1) - timedelta(days=1)

        # Fetch all active employees
        employees = self.env['hr.employee'].search([])

        if not employees:
            return

        for employee in employees:

            # Check if the employee already has a payslip for the specified period
            existing_payslip = self.env['hr.payslip'].search([
                ('employee_id', '=', employee.id),
                ('date_from', '=', start_date.strftime('%Y-%m-%d')),
                ('date_to', '=', end_date.strftime('%Y-%m-%d')),
                ('state', '!=', 'cancel')  # Exclude canceled payslips
            ])

            if existing_payslip:
                # Skip employee if payslip already exists for this period
                continue

            contract = employee.contract_id
            if not contract:
                continue

            # Get the payroll structure from the employee's contract
            payroll_structure_type = contract.struct_id
            if not payroll_structure_type:
                continue
            # Create a payslip for each employee
            payslip = self.env['hr.payslip'].create({
                'employee_id': employee.id,
                'date_from': start_date.strftime('%Y-%m-%d'),
                'date_to': end_date.strftime('%Y-%m-%d'),
                'struct_id': payroll_structure_type.id,
            })

            # Compute the payslip
            payslip.compute_sheet()

        return True
