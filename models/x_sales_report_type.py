# -*- coding: utf-8 -*-
"""x_sales_report_type - report catalog model.

Adopted from BugFix-Accounting where it lived alongside sentinel copies
in BugFix-Stock, BugFix-MRP and BugFix-Sales. Consolidating to a single
owner here eliminates the load-order cycle that blocked cross-repo O2M
navigation and forced the v0.0.31 tab/column strips in BugFix-Accounting.

All 5 stock/mrp-side One2manys (previously TODO in BugFix-Accounting's
model file, previously stripped from x_sales_report_type_studio_ported_v2.xml
tree extension) are declared here because their inverse M2Os on stock.move,
stock.move.line, mrp.production also live in this module.
"""
from odoo import fields, models


class XSalesReportType(models.Model):
    _name = 'x_sales_report_type'
    _description = 'X Sales Report Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Report Name')
    x_studio_report_code = fields.Selection([], string='Report Code')
    x_studio_sequence = fields.Integer(string='Sequence')

    # ------------------------------------------------------------------
    # One2many navigation - inverse M2Os all live in this module
    # ------------------------------------------------------------------
    x_studio_journal_entry_id = fields.One2many(
        'account.move',
        'x_studio_report_type_s_cust_aging',
        string='Journal Entry Id',
    )
    x_studio_journal_items_id = fields.One2many(
        'account.move.line',
        'x_studio_sales_report_type',
        string='Journal Items Id',
    )
    x_studio_sales_lines_id = fields.One2many(
        'sale.order.line',
        'x_studio_sales_report_type',
        string='Sales Lines Id',
    )
    x_studio_test = fields.One2many(
        'account.move.line',
        'x_studio_many2one_field_kiSUJ',
        string='test',
    )

    # Stock/MRP-side O2Ms - restored from the BugFix-Accounting v0.0.31
    # tree-column strips. Cycle is now resolved because both sides live
    # in this module.
    x_studio_prod_summary_split_id = fields.One2many(
        'stock.move.line',
        'x_studio_report_type_production_summary_split',
        string='Prod. Summary Split Id',
    )
    x_studio_production_order_id = fields.One2many(
        'mrp.production',
        'x_studio_report_type_m_wip',
        string='Production Order Id',
    )
    x_studio_production_variance_id = fields.One2many(
        'stock.move',
        'x_studio_report_type_production_job_variance',
        string='Production Variance Id',
    )
    x_studio_sales_prod_purch_id = fields.One2many(
        'stock.move.line',
        'x_studio_report_type_sales_prod_purch',
        string='Sales Prod. Purch. Id',
    )
    x_studio_slow_moving_item_id = fields.One2many(
        'stock.move.line',
        'x_studio_report_type_slow_moving_items',
        string='Slow Moving Item Id',
    )
