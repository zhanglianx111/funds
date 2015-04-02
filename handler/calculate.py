#!/usr/bin/env python
# coding=utf-8

import log
import json
import datetime
from time import mktime, strptime
from setting import *
from database import DB

logger = log.getMyLogger(__name__)


def handler_calc(args):
    if args is None:
        logger.error("args is None")
        return "args is None"

    print args
    # return
    name = args.name
    frm = args.frm
    to = args.to
    sort = args.sort
    count = args.count

    '''
    if frm is None:
        fYear = G_YEAR
        fMonth = G_MONTH
        fDay = G_DAY
    else:
        if len(frm.split('.')) != 3:
            return "from date format is error"
        fYear = int(frm.split('.')[0])
        fMonth = int(frm.split('.')[1])
        fDay = int(frm.split('.')[2])

    fYear = 2015
    fMonth = 3
    fDay 3
    fromDate = [fYear, fMonth, fDay]

    if to is None or len(to.split('.')) != 3:
        return "to date is error"

    tYear = int(to.split('.')[0])
    tMonth = int(to.split('.')[1])
    tDay = int(to.split('.')[2])
    toDate = [tYear, tMonth, tDay]
    #print "to date is:", tYear, tMonth, tDay

    '''

    if DB.client is None:
        logger.error("can not find DB")
        return "can not find DB"

    db = DB.get_db(G_DB_FUNDS)
    if db is None:
        logger.error("get database(%s) failed" % (G_DB_FUNDS))
        return "get database(%s) failed" % (G_DB_FUNDS)

    col_daily = DB.create_col(db, G_TABLE_RECORD_DAILY)
    if col_daily is None:
        logger.error("can not get collection(%s)" % G_TABLE_RECORD_DAILY)
        return "can not get collection(%s)" % G_TABLE_RECORD_DAILY

    if frm is None:
        fromDate = getYesterday().strftime("%Y-%m-%d").split("-")
        print fromDate    
    else:
        if len(frm.split('.')) != 3:
             return "from date format is error"
        fYear = int(frm.split('.')[0])
        fMonth = int(frm.split('.')[1])
        fDay = int(frm.split('.')[2])
        fromDate = [fYear, fMonth, fDay]     

    if name is not None:
        calc_single(name, fromDate, toDate, col_daily)
        return
    else:
        calc_all(fromDate, toDate, count, sort, col_daily)
        return


def calc_single(name, f, t, collection):
    col_daily = collection

    fdFrom = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: datetime.datetime(
            f[0],
            f[1],
            f[2])}
    pFrom = DB.find_one(col_daily, fdFrom)
    if pFrom is None:
        print "no serach data at from:", f
        return
    # print "from:", pFrom

    fdTo = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: datetime.datetime(
            t[0],
            t[1],
            t[2])}
    pTo = DB.find_one(col_daily, fdTo)
    if pTo is None:
        print "no serach data at to:", t
        return

    # print "to:", pTo
    fDwjz = float(pFrom['dwjz'])
    tDwjz = float(pTo['dwjz'])

    inc = (tDwjz - fDwjz) / fDwjz
    print f, ":", fDwjz, "-->", t, ":", tDwjz, ", inc:", inc * 100, "%", ", jjdm:", pTo['jjdm']
    print ""
    print ".3f(%s) --> .3f(%s)" % (fDwjz, datetime.datetime(t[0], t[1], t[2]))
    return


def calc_all(fDate, tDate, count, srt, col_daily):
    cnt = 0
    for post in DB.find_all(col_daily):
        if post is not None and cnt < count:
            cnt += 1
            print post

'''
def isNowTime(frm):
    IsNowTime
    参数：
        time：datetime格式的时间
    功能：
        time和给定的时间（全局的一个时间点，在setting中定义）转化为时间戳。比较两者的时间戳，如果为负则认为传入的时间在给定的时间点之前；如果为正则认为在给定的时间之后。
    
    t1 = mktime(strptime(frm.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S"))
    t2 = mktime(strptime(TIME))

    return t1 - t2
'''

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday
