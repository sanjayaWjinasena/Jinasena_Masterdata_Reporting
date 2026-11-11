"""Inverse M2Os for sales_report_type One2manys targeting
account.move.line. Adopted from BugFix-Accounting/models/account_move_line.py.
"""

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # Inverse of sales_report_type.journal_items_id
    sales_report_type = fields.Many2one(
        "sales_report_type",
        string="Report Type (S- Incentive Calculation)",
    )

    # Inverse of sales_report_type.test
    many2one_field_kiSUJ = fields.Many2one(
        "sales_report_type",
        string="Sales Report Type",
    )
