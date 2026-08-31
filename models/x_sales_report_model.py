# -*- coding: utf-8 -*-
"""x_sales_report_model - report record instance model.

Adopted from BugFix-Accounting. The 16 direct One2many fields to x_rm_*
target models (which live in BugFix-Accounting) are NOT declared here -
they're added via _inherit in BugFix-Accounting's own model file since
their inverse M2Os on x_rm_* only exist when BugFix-Accounting is loaded.

Related One2manys navigating through x_studio_report_type all have their
intermediate hop declared in x_sales_report_type in this module, so they
resolve safely at masterdata load time.
"""
from odoo import fields, models


class XSalesReportModel(models.Model):
    _name = 'x_sales_report_model'
    _description = 'X Sales Report Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')

    # ------------------------------------------------------------------
    # Scalar fields (accounting/reporting scalars, OH/cost/GP/etc.)
    # ------------------------------------------------------------------
    x_studio_actual_gp_ = fields.Float(string='Actual GP')
    x_studio_actuals = fields.Boolean(string='Actuals')
    x_studio_as_on_date = fields.Date(string='As on Date')
    x_studio_as_on_date_1 = fields.Date(string='From Date')
    x_studio_as_on_date_2 = fields.Date(string='To Date')
    x_studio_auto_generated = fields.Boolean(string='Auto Generated')
    x_studio_contingency_ = fields.Float(string='Contingency %')
    x_studio_created_date = fields.Date(string='Created Date')
    x_studio_date_updated = fields.Boolean(string='Date Updated')
    x_studio_distributor_addition = fields.Float(string='Distributor Addition %')
    x_studio_estimated_gp_ = fields.Float(string='Estimated GP')
    x_studio_factory_oh = fields.Float(string='Factory OH')
    x_studio_factory_oh_labour = fields.Float(string='Factory OH (Labour)')
    x_studio_financial_progress = fields.Float(string='Financial Progress')
    x_studio_from_date = fields.Date(string='From Date')
    x_studio_idling_rate = fields.Float(string='Idling Rate %')
    x_studio_management_purpose = fields.Boolean(string='Management Purpose')
    x_studio_month_end_entry_updated = fields.Boolean(string='Month End Entry Updated')
    x_studio_oh_absorbed_2_factory = fields.Float(string='OH Absorbed 2 (Factory)')
    x_studio_oh_absorbed_2_other = fields.Float(string='OH Absorbed 2 (Other)')
    x_studio_oh_absorbed_2_sales = fields.Float(string='OH Absorbed 2 (Sales)')
    x_studio_oh_absorbed_factory = fields.Float(string='OH Absorbed (Factory)')
    x_studio_oh_absorbed_other = fields.Float(string='OH Absorbed (Other)')
    x_studio_oh_absorbed_sales = fields.Float(string='OH Absorbed (Sales)')
    x_studio_other_oh = fields.Float(string='Other OH')
    x_studio_profit_mark_up_ = fields.Float(string='Profit Mark Up %')
    x_studio_report_code = fields.Selection([], string='Report Code')
    x_studio_sales_oh = fields.Float(string='Sales OH')
    x_studio_selection_field_Fbw0x = fields.Selection([], string='Status')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sscl = fields.Float(string='SSCL %')

    # ------------------------------------------------------------------
    # Many2one to standard-Odoo models
    # ------------------------------------------------------------------
    x_studio_created_from_project_update = fields.Many2one('project.update', string='Created From Project Update')
    x_studio_customer = fields.Many2many('res.partner', 'x_sales_report_model_x_studio_customer_rel', 'host_id', 'target_id', string='Customer')
    x_studio_project_no = fields.Many2one('project.project', string='Project No')
    x_studio_report_type = fields.Many2one('x_sales_report_type', string='Report Type')
    x_studio_sales_centre = fields.Many2many('crm.team', 'x_sales_report_model_x_studio_sales_centre_rel', 'host_id', 'target_id', string='Sales Centre')

    # ------------------------------------------------------------------
    # Direct One2many to x_rm_* target models NOT declared here.
    # Their inverse M2O fields (x_studio_sales_report_model_id on each
    # x_rm_*) live in BugFix-Accounting. Adding them here would require
    # a BugFix-Accounting dep which we can't have. BugFix-Accounting
    # adds all 16 via _inherit on x_sales_report_model.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Related One2many navigation via x_studio_report_type
    # All intermediate targets live in x_sales_report_type in this module.
    # ------------------------------------------------------------------
    x_studio_journal_item_ids = fields.One2many(
        'account.move.line',
        related='x_studio_report_type.x_studio_journal_items_id',
        string='Journal Item Ids',
        readonly=True,
    )
    x_studio_related_field_DqBBB = fields.One2many(
        'sale.order.line',
        related='x_studio_report_type.x_studio_sales_lines_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_n589a = fields.One2many(
        'account.move.line',
        related='x_studio_report_type.x_studio_journal_items_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_nfrkz = fields.One2many(
        'account.move',
        related='x_studio_report_type.x_studio_journal_entry_id',
        string='New Related Field',
        readonly=True,
    )
    # Stock/MRP related O2Ms - restored from BugFix-Accounting v0.0.31
    # tab strips. Cycle resolved.
    x_studio_related_field_NsCKm = fields.One2many(
        'stock.move.line',
        related='x_studio_report_type.x_studio_sales_prod_purch_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_PaCjA = fields.One2many(
        'stock.move',
        related='x_studio_report_type.x_studio_production_variance_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_XCKXu = fields.One2many(
        'stock.move.line',
        related='x_studio_report_type.x_studio_slow_moving_item_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_bCtVj = fields.One2many(
        'stock.move.line',
        related='x_studio_report_type.x_studio_prod_summary_split_id',
        string='New Related Field',
        readonly=True,
    )
    x_studio_related_field_oeTJK = fields.One2many(
        'mrp.production',
        related='x_studio_report_type.x_studio_production_order_id',
        string='New Related Field',
        readonly=True,
    )
