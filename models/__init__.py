# -*- coding: utf-8 -*-
# Inverse M2O extensions loaded FIRST so target fields exist by the time
# x_sales_report_type declares its One2manys against them.
from . import account_move
from . import account_move_line
from . import sale_order_line
from . import stock_move
from . import stock_move_line
from . import mrp_production
from . import x_sales_report_type
from . import x_sales_report_model
