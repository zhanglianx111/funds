#!/usr/bin/env python
# coding=utf-8

import log
import heapq
import operator
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
        print "can not found DB"
        return "can not find DB"

    db = DB.get_db(G_DB_FUNDS)
    if db is None:
        logger.error("get database(%s) failed" % (G_DB_FUNDS))
        return "get database(%s) failed" % (G_DB_FUNDS)

    col_daily = DB.create_col(db, G_TABLE_RECORD_DAILY)
    col_index = DB.create_col(db, G_TABLE_FUNDS_INDEX)
    if col_daily is None or col_index is None:
        logger.error("can not get collection(%s or %s)" % (G_TABLE_RECORD_DAILY, G_TABLE_FUNDS_INDEXi))
        return "can not get collection(%s)" % (G_TABLE_RECORD_DAILY,G_TABLE_FUNDS_INDEX)


    if frm is None:
        fromDate = getSomeday(date.today().strftime('%Y-%m-%d'), 1).strftime('%Y-%m-%d')
    else:
        if len(frm.split('.')) != 3:
            return "from date format is error"
    
        fromDate = datetime.strptime(frm, "%Y.%m.%d").strftime('%Y-%m-%d')

    if name is not None:
        calc_single(name, fromDate, to, col_daily, col_index, 1)
        return
    else:
        calc_all(fromDate, to, count, sort, col_daily, col_index, 0)
        return


def calc_single(name, f, delta, daily_col, index_col, prnt):
    logger.debug("name:%s, from day:%s, delta:%d" % (name, f, delta))
    col_daily = daily_col
    col_index = index_col

    fdFrom = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: datetime.strptime(f, '%Y-%m-%d'),
    }
    pFrom = DB.find_one(col_daily, fdFrom)
    if pFrom is None:
        #print "no serach data at from: %s, %s" % (f, name)
        logger.error("no serach data at from: %s, %s" % (f, name))
        pFrom = {G_NAME_JJDM: name, G_NAME_DWJZ:'0'}

    sday = getSomeday(f, delta)
    fdTo = {
        G_NAME_JJDM: name,
        G_NAME_JLRQ: sday
    }
    pTo = DB.find_one(col_daily, fdTo)
    if pTo is None:
        #print "no serach data at to: %s, %s" % (sday, name) 
        logger.error("no serach data at to: %s, %s" % (sday, name))
        pTo = {G_NAME_JJDM: name, G_NAME_DWJZ:'0'}

    fdIndex = {
        G_NAME_JJDM: name
    }
    index = DB.find_one(col_index, fdIndex)
    if index is None:
        logger.debug("no found jjdm:%s" %(name))
        print "no found jjdm:", name
        return {}

    mz = index[G_NAME_JJMZ]
    if len(pFrom['dwjz']) == 0 or len(pTo['dwjz'])  == 0:
        fDwjz = tDwjz = 0
    else:
        fDwjz = float(pFrom['dwjz'])
        tDwjz = float(pTo['dwjz'])
    
    if fDwjz == 0:
        inc = 0
    else:
        inc = (tDwjz - fDwjz) / fDwjz
    if prnt == 1: 
        if delta <= 0:
            print "%.4f%%  %s  %s  %s(%s) --> %s(%s)" % (inc*100,  pTo[G_NAME_JJDM], mz, fDwjz, f, tDwjz, sday)
        else:
            print "%.4f%%  %s  %s  %s(%s) --> %s(%s)" % (-inc*100, pTo[G_NAME_JJDM], mz, tDwjz, sday, fDwjz, f)
    
    return {'jjdm': pTo['jjdm'], 'jjmz': mz, 'inc': inc}


def calc_all(fDate, tDate, count, srt, daily_col, index_col, prnt):
    cnt = 0
    r_index = []

    for idx in DB.find_all(index_col):
        tmp_r = None
        tmp_r = calc_single(idx['jjdm'], fDate, tDate, daily_col, index_col, 0)
        if tmp_r != {}:
            r_index.append(tmp_r)

    #print r_index
    if srt == '-':
        flag = True
    else:
        flag = False

    sorted_inc = sorted(r_index, key=operator.itemgetter('inc'), reverse=flag)
    for i in range(len(sorted_inc)):
        print "%.4f%%  jjdm: %s  jjmz: %s" % (sorted_inc[i]['inc']*100, sorted_inc[i][G_NAME_JJDM], sorted_inc[i][G_NAME_JJMZ])
        if i >= count:
            break

    return

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
