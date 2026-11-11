"""Inverse M2O for sales_report_type.production_variance_id.
Adopted from BugFix-Stock/models/stock_move.py.
"""

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    report_type_production_job_variance = fields.Many2one(
        "sales_report_type",
        string="Report Type - Production Job Variance",
    )
