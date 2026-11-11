"""Inverse M2Os for sales_report_type One2manys targeting stock.move.line.
Adopted from BugFix-Stock/models/stock_move_line.py.
"""

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    # Inverse of sales_report_type.prod_summary_split_id
    report_type_production_summary_split = fields.Many2one(
        "sales_report_type",
        string="Report Type - Production Summary Split",
    )

    # Inverse of sales_report_type.sales_prod_purch_id
    report_type_sales_prod_purch = fields.Many2one(
        "sales_report_type",
        string="Report Type - Sales prod. purch.",
    )

    # Inverse of sales_report_type.slow_moving_item_id
    report_type_slow_moving_items = fields.Many2one(
        "sales_report_type",
        string="Report Type - Slow Moving Items",
    )
