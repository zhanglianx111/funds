#!/usr/bin/env python
# coding=utf-8

G_URL = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,'
G_OTHERS = '&dt=1424049754634&atfc=%onlySale=0'

G_TOTAL = '2500'
G_ONCE = 400

G_JJDM = 0
G_JJMZ = 1
G_DWJZ = 3
G_SGZT = 9

G_DB_FUND = 'fund'

G_TABLE_FUND_INDEX = 'index'
G_TABLE_RECORD_DAILY = 'daily'
G_TABLE_FUNDS_BOUGHT = 'buy'

# 下列字段用于buy表 
# 买入基金代码
G_FUND_INDEX = 'fund_index'

# 买入金额
G_MONEY = 'money'

# 购买日期
G_DATE_BUY = 'buy'

# 卖出日期
G_DATE_SELL = 'sell'

# 购入份额 
G_FUND_UNIT = 'unit'


# log
G_log_name = 'funds.log' 
g_log_dir = '/var/log/'
