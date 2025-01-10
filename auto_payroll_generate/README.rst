# Payroll Auto Generate Module for Odoo 15

## Overview
The **Payroll Auto Generate** module automates the payroll generation process in Odoo 15. It creates and computes payslips for all employees of a company based on a defined schedule.

### Key Features
- Automatically generates payroll on a scheduled date.
- Calculates payslips for all employees in the company.
- Supports scheduled actions to run payroll at regular intervals (e.g., monthly).
- Computes payslip details using the built-in `compute_sheet` function.

---

## Installation

### Step 1: Copy the Module
1. Place the module folder (`payroll_auto_generate`) in the `addons` directory of your Odoo installation.
   ```
   /path/to/odoo/addons/payroll_auto_generate
   ```

### Step 2: Restart Odoo Server
Restart the Odoo server to recognize the new module.
```bash
sudo service odoo restart
```

### Step 3: Install the Module
1. Go to **Apps** in the Odoo interface.
2. Search for "Payroll Auto Generate."
3. Click **Install** to activate the module.

---

## Usage

### Scheduled Action
- The module sets up a scheduled action that runs on the **1st of each month** by default.
- It calculates payroll for the **previous month** (e.g., runs on Nov 1, 2024, for the period Oct 1 - Oct 31, 2024).

You can customize the schedule:
1. Go to **Settings > Technical > Scheduled Actions.**
2. Search for "Auto Generate Payroll."
3. Adjust the frequency and next execution date as needed.

---

## How It Works

### Automated Payroll Process
1. On the scheduled date, the system:
   - Fetches all active employees.
   - Determines the payroll period (previous month).
   - Generates a payslip for each employee.
   - Computes the payslip details using the `compute_sheet` method.

2. The payslips are stored in **Payroll > Payslips**, where they can be reviewed, validated, and processed further.

---

## Configuration

### Database Setup
Ensure the payroll structure and journal configurations are already set up in Odoo:
1. Go to **Payroll > Configuration > Salary Structures.**
2. Define the required salary rules and structure types.

### Scheduled Action
To modify the default schedule:
1. Navigate to **Settings > Technical > Scheduled Actions.**
2. Edit the **Auto Generate Payroll** action.
3. Set a new interval, next execution date, or custom code if needed.

---

## Module Details

### Folder Structure
```
payroll_auto_generate/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── payroll_auto_generate.py
├── data/
│   └── scheduled_action.xml
```

### Key Files
1. **`__manifest__.py`:** Contains module metadata.
2. **`models/payroll_auto_generate.py`:** Implements the core logic for payroll generation.
3. **`data/scheduled_action.xml`:** Defines the scheduled action for automatic payroll.

---

## Customization

### Changing Payroll Period
If you need a different payroll period (e.g., bi-weekly or custom dates), modify the date logic in `payroll_auto_generate.py`:
```python
start_date = ...  # Define your custom start date logic
end_date = ...    # Define your custom end date logic
```

### Adding Filters for Specific Employees
To generate payroll only for a specific group of employees, update the `employees` query:
```python
employees = self.env['hr.employee'].search([('department_id', '=', specific_department_id)])
```

---

## Support
For any issues or feature requests, please contact:
- **Author:** NexOrionis Techsphere
- **Email:** nexorionis.info@gmail.com

