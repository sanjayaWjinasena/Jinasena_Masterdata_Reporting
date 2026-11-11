"""Inverse M2O for sales_report_type.sales_lines_id.
Adopted from BugFix-Sales/models/sale_order_line.py.
"""

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sales_report_type = fields.Many2one(
        "sales_report_type",
        string="Sales Report Type",
    )
