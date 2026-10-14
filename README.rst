Reporting Masterdata
====================

Adopted from previously duplicated declarations in BugFix-Accounting,
BugFix-Stock, BugFix-MRP and BugFix-Sales. Each of those had its own
sentinel `_name = 'x_sales_report_type'` scaffold; consolidating to a
single owner here eliminates the load-order cycle that blocked cross-
repo O2M navigation.

Downstream repos convert their sentinel files to _inherit-only (or
delete them entirely) and add this module to their `depends` list.

Information
-----------

* Technical name: ``Jinasena_Masterdata_Reporting``
* Version: ``17.0.1.0.6``
* Depends on: ``base_setup``, ``account``, ``sale``, ``stock``, ``mrp``
* Author: Jinasena Agricultural Machinery (Pvt) Ltd.
* License: LGPL-3

Further documentation
---------------------

* Functional documentation: ``Functional_Documentation.md``
* Change history: ``CHANGELOG.md``
