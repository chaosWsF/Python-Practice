import tablib
import pandas as pd
import numpy as np


def log_cash(context, bar_dict):
    logger.info("Remaining cash: %r" % context.portfolio.cash)


def init(context):

    # Report the remaining cash every day or every week.
    # scheduler.run_daily(log_cash)
    scheduler.run_weekly(log_cash)

    # in sample period
    start_date = '2014-01-01'
    end_date = '2017-12-31'

    code_list = all_instruments(type='CS').order_book_id.values
    nost_index = []
    for i in range(len(code_list)):
        if not is_st_stock(code_list[i], count=1):
            nost_index.append(i)
    code_list = code_list[nost_index]
    context.dataset = get_price(
        code_list, 
        start_date=start_date, end_date=end_date, 
        adjust_type='pre'
    )

    # TODO: Here are the models -> selected stock codes and respective amount

    context.stock = ['600519.XSHE']
    context.amount = [100]


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    
    stock = context.stock
    amount = context.amount

    # TODO: Here is the strategy -> real amount and real stock

    today_stock = stock
    today_amount = amount

    for i in range(len(stock)):
        order_shares(today_stock[i], today_amount[i])


def after_trading(context):
    pass
