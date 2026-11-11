"""sales_report_model - report record instance model.

Adopted from BugFix-Accounting. The 16 direct One2many fields to x_rm_*
target models (which live in BugFix-Accounting) are NOT declared here -
they're added via _inherit in BugFix-Accounting's own model file since
their inverse M2Os on x_rm_* only exist when BugFix-Accounting is loaded.

Related One2manys navigating through report_type all have their
intermediate hop declared in sales_report_type in this module, so they
resolve safely at masterdata load time.
"""

from odoo import fields, models


class XSalesReportModel(models.Model):
    _name = "sales_report_model"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "X Sales Report Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    active = fields.Boolean()
    name = fields.Char()

    # ------------------------------------------------------------------
    # Scalar fields (accounting/reporting scalars, OH/cost/GP/etc.)
    # ------------------------------------------------------------------
    actual_gp_ = fields.Float(string="Actual GP")
    actuals = fields.Boolean()
    as_on_date = fields.Date(string="As on Date")
    as_on_date_1 = fields.Date(string="From Date")
    as_on_date_2 = fields.Date(string="To Date")
    auto_generated = fields.Boolean()
    contingency_ = fields.Float(string="Contingency %")
    created_date = fields.Date()
    date_updated = fields.Boolean()
    distributor_addition = fields.Float(string="Distributor Addition %")
    estimated_gp_ = fields.Float(string="Estimated GP")
    factory_oh = fields.Float(string="Factory OH")
    factory_oh_labour = fields.Float(string="Factory OH (Labour)")
    financial_progress = fields.Float()
    from_date = fields.Date()
    idling_rate = fields.Float(string="Idling Rate %")
    management_purpose = fields.Boolean()
    month_end_entry_updated = fields.Boolean()
    oh_absorbed_2_factory = fields.Float(string="OH Absorbed 2 (Factory)")
    oh_absorbed_2_other = fields.Float(string="OH Absorbed 2 (Other)")
    oh_absorbed_2_sales = fields.Float(string="OH Absorbed 2 (Sales)")
    oh_absorbed_factory = fields.Float(string="OH Absorbed (Factory)")
    oh_absorbed_other = fields.Float(string="OH Absorbed (Other)")
    oh_absorbed_sales = fields.Float(string="OH Absorbed (Sales)")
    other_oh = fields.Float(string="Other OH")
    profit_mark_up_ = fields.Float(string="Profit Mark Up %")
    report_code = fields.Selection(
        string="Report Code",
        related="report_type.report_code",
        store=True,
        readonly=True,
    )
    sales_oh = fields.Float(string="Sales OH")
    selection_field_Fbw0x = fields.Selection(
        [("Draft", "Draft"), ("Done", "Done")], string="Status"
    )
    sequence = fields.Integer()
    sscl = fields.Float(string="SSCL %")

    # ------------------------------------------------------------------
    # Many2one to standard-Odoo models
    # ------------------------------------------------------------------
    created_from_project_update = fields.Many2one("project.update")
    customer = fields.Many2many(
        "res.partner",
        "x_sales_report_model_x_studio_customer_rel",
        "host_id",
        "target_id",
    )
    project_no = fields.Many2one("project.project")
    report_type = fields.Many2one("sales_report_type")
    sales_centre = fields.Many2many(
        "crm.team",
        "x_sales_report_model_x_studio_sales_centre_rel",
        "host_id",
        "target_id",
    )

    # ------------------------------------------------------------------
    # Direct One2many to x_rm_* target models NOT declared here.
    # Their inverse M2O fields (sales_report_model_id on each
    # x_rm_*) live in BugFix-Accounting. Adding them here would require
    # a BugFix-Accounting dep which we can't have. BugFix-Accounting
    # adds all 16 via _inherit on sales_report_model.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Related One2many navigation via report_type
    # All intermediate targets live in sales_report_type in this module.
    # ------------------------------------------------------------------
    journal_item_ids = fields.One2many(
        "account.move.line",
        related="report_type.journal_items_id",
        string="Journal Item Ids",
        readonly=True,
    )
    related_field_DqBBB = fields.One2many(
        "sale.order.line",
        related="report_type.sales_lines_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_n589a = fields.One2many(
        "account.move.line",
        related="report_type.journal_items_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_nfrkz = fields.One2many(
        "account.move",
        related="report_type.journal_entry_id",
        string="New Related Field",
        readonly=True,
    )
    # Stock/MRP related O2Ms - restored from BugFix-Accounting v0.0.31
    # tab strips. Cycle resolved.
    related_field_NsCKm = fields.One2many(
        "stock.move.line",
        related="report_type.sales_prod_purch_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_PaCjA = fields.One2many(
        "stock.move",
        related="report_type.production_variance_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_XCKXu = fields.One2many(
        "stock.move.line",
        related="report_type.slow_moving_item_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_bCtVj = fields.One2many(
        "stock.move.line",
        related="report_type.prod_summary_split_id",
        string="New Related Field",
        readonly=True,
    )
    related_field_oeTJK = fields.One2many(
        "mrp.production",
        related="report_type.production_order_id",
        string="New Related Field",
        readonly=True,
    )
