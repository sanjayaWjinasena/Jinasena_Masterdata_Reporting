# -*- coding: utf-8 -*-
"""Inverse M2O for x_sales_report_type.x_studio_production_variance_id.
Adopted from BugFix-Stock/models/stock_move.py.
"""
from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    x_studio_report_type_production_job_variance = fields.Many2one(
        'x_sales_report_type',
        string='Report Type - Production Job Variance',
    )
