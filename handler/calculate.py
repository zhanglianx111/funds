#!/usr/bin/env python
# coding=utf-8

import log
from datetime import datetime, date, timedelta
from database import DB
from setting import *

logger = log.getMyLogger(__name__)


def handler_calc(args):
    if args is None:
        logger.error("args is None")
        return "args is None"

    name = args.name
    frm = args.frm
    to = args.to
    sort = args.sort
    count = args.count

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
        fromDate = getSomeday(date.today().strftime('%Y-%m-%d'), 1).strftime('%Y-%m-%d')
    else:
        if len(frm.split('.')) != 3:
            return "from date format is error"
    
        fromDate = datetime.strptime(frm, "%Y.%m.%d").strftime('%Y-%m-%d')
    if name is not None:
        calc_single(name, fromDate, to, col_daily)
        return
    else:
        calc_all(fromDate, to, count, sort, col_daily)
        return


def calc_single(name, f, delta, collection):
    logger.debug("name:%s, from day:%s, delta:%d" % (name, f, delta))
    col_daily = collection

    fdFrom = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: datetime.strptime(f, '%Y-%m-%d'),
    }
    pFrom = DB.find_one(col_daily, fdFrom)
    if pFrom is None:
        print "no serach data at from:", f
        return
    
    sday = getSomeday(f, delta)
    fdTo = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: sday
    }
    pTo = DB.find_one(col_daily, fdTo)
    if pTo is None:
        print "no serach data at to:", sday 
        return

    fDwjz = float(pFrom['dwjz'])
    tDwjz = float(pTo['dwjz'])
    
    inc = (tDwjz - fDwjz) / fDwjz
    if delta <= 0:
        print f, ":", fDwjz, "-->", sday, ":", tDwjz, ", inc:", inc * 100, "%", ", jjdm:", pTo['jjdm']
        print ""
    else:
        print sday, ":", tDwjz, "-->", f, ":", fDwjz, ", inc:", -inc * 100, "%", ", jjdm:", pTo['jjdm'] 
        print
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


def getSomeday(start, delta):
    '''getSomeday
    day: type is string
    delta: type is int
    '''
    start = datetime.strptime(start, '%Y-%m-%d')
    days = timedelta(days=delta)
    smday = start - days
    return smday
