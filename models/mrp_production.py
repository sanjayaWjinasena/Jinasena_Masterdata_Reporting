"""Inverse M2O for sales_report_type.production_order_id.
Adopted from BugFix-MRP/models/mrp_production.py.
"""

from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    report_type_m_wip = fields.Many2one(
        "sales_report_type",
        string="Report Type (M-WIP)",
    )
