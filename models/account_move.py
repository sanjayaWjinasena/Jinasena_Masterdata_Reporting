# -*- coding: utf-8 -*-
"""Inverse M2O for x_sales_report_type.x_studio_journal_entry_id.
Adopted from BugFix-Accounting/models/account_move.py where it lived
alongside the model itself.
"""
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_studio_report_type_s_cust_aging = fields.Many2one(
        'x_sales_report_type',
        string='Report Type (S - Cust Aging)',
    )
