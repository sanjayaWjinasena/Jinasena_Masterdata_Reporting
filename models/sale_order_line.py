# -*- coding: utf-8 -*-
"""Inverse M2O for x_sales_report_type.x_studio_sales_lines_id.
Adopted from BugFix-Sales/models/sale_order_line.py.
"""
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_studio_sales_report_type = fields.Many2one(
        'x_sales_report_type',
        string='Sales Report Type',
    )
