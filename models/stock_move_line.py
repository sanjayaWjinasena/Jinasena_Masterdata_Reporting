# -*- coding: utf-8 -*-
"""Inverse M2Os for x_sales_report_type One2manys targeting stock.move.line.
Adopted from BugFix-Stock/models/stock_move_line.py.
"""
from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    # Inverse of x_sales_report_type.x_studio_prod_summary_split_id
    x_studio_report_type_production_summary_split = fields.Many2one(
        'x_sales_report_type',
        string='Report Type - Production Summary Split',
    )

    # Inverse of x_sales_report_type.x_studio_sales_prod_purch_id
    x_studio_report_type_sales_prod_purch = fields.Many2one(
        'x_sales_report_type',
        string='Report Type - Sales prod. purch.',
    )

    # Inverse of x_sales_report_type.x_studio_slow_moving_item_id
    x_studio_report_type_slow_moving_items = fields.Many2one(
        'x_sales_report_type',
        string='Report Type - Slow Moving Items',
    )
