#!/usr/bin/env python
# coding=utf-8
from datetime import date

G_URL = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,'
G_OTHERS = '&dt=1424049754634&atfc=%onlySale=0'

G_TOTAL = '2500'
G_ONCE = 400

'''jjdm:基金代码
   jjmz:基金名字
   dwjz:单位净值
   sgzt:申购状态
   jlrq:记录日期
'''
G_JJDM = 0
G_JJMZ = 1
G_DWJZ = 3
G_SGZT = 9

G_NAME_JJDM = 'jjdm'
G_NAME_JJMZ = 'jjmz'
G_NAME_DWJZ = 'dwjz'
G_NAME_SGZT = 'gszt'
G_NAME_JLRQ = 'jlrq'

G_DB_FUNDS = 'funds'

G_TABLE_FUNDS_INDEX = 'index'
G_TABLE_RECORD_DAILY = 'daily'
G_TABLE_FUNDS_BOUGHT = 'buy'

# 下列字段用于buy表 
# 买入基金代码
G_FUNDS_INDEX = 'funds_index'

# 买入金额
G_MONEY = 'money'

# 购买日期
G_DATE_BUY = 'buy'

# 卖出日期
G_DATE_SELL = 'sell'

# 购入份额 
G_FUND_UNIT = 'unit'


# log
G_LOG_NAME = 'funds.log' 
G_LOG_DIR = '/var/log/'
#G_LOG_LEVEL = logging.INFO

# mongodb
G_HOST = '127.0.0.1'
G_PORT = 27017

# date
G_YEAR = date.today().year
G_MONTH = date.today().month
G_DAY = date.today().day
