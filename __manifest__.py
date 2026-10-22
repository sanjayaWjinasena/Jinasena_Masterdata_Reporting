{
    "name": "Jinasena : SubModule : Reporting : Masterdata",
    "version": "17.0.1.0.6",
    "summary": (
        "Cross-cutting reporting masterdata for the Jinasena Odoo "
        "installation. Owns x_sales_report_type + x_sales_report_model - "
        "the report catalog + report record models that Sales, Accounting, "
        "Stock and MRP all consume. Also owns the inverse Many2one fields "
        "those models' One2manys navigate through, on account.move, "
        "account.move.line, sale.order.line, stock.move, stock.move.line, "
        "and mrp.production."
    ),
    "author": "Jinasena Agricultural Machinery (Pvt) Ltd.",
    "category": "Extra Tools",
    "license": "LGPL-3",
    # v17.0.1.0.2: shared Jinasena icon added at static/description/icon.png.
    # Cross-module audit confirmed zero real gap on this module's scope
    # (x_sales_report_model + x_sales_report_type):
    #   Fields: 0 gap  |  Views: 0 gap  |  Server actions: 0 (+3 ir_cron skipped)
    #   Base.automations: 0 gap  |  Window actions: 0 gap
    # 100% coverage across all categories.
    "depends": ["base_setup", "account", "sale", "stock", "mrp"],
    "data": [
        "security/ir_model_pins.xml",
        "security/ir.model.access.csv",
        "data/window_actions_backlog.xml",
    ],
    # Note: primary views (Default form/tree/search) stay in
    # BugFix-Accounting for now. Views don't need to live in the same
    # module as the model they render. Moving them would require
    # splitting the _v2.xml files which mix primaries + extensions -
    # not worth the risk on the first migration pass. Follow-up.
}
