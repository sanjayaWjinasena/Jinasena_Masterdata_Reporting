# -*- coding: utf-8 -*-
"""Inverse M2O for x_sales_report_type.x_studio_production_order_id.
Adopted from BugFix-MRP/models/mrp_production.py.
"""
from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    x_studio_report_type_m_wip = fields.Many2one(
        'x_sales_report_type',
        string='Report Type (M-WIP)',
    )
