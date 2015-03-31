#!/usr/bin/env python
# coding=utf-8

import log
import json
import datetime
from setting import *
from database import DB

logger = log.getMyLogger(__name__)


def handler_calc(args):
    if args is None:
        logger.error("args is None")
        return "args is None"

    print args
    name = args.name
    frm = args.frm
    to = args.to
    sort = args.sort
    count = args.count

    if frm is None:
        fYear = G_YEAR
        fMonth = G_MONTH
        fDay = G_DAY
    else:
        print frm.split('.')    
        if len(frm.split('.')) != 3:
            return "from date format is error"
        fYear = int(frm.split('.')[0])
        fMonth = int(frm.split('.')[1])
        fDay = int(frm.split('.')[2])

    print "from date is:", fYear, fMonth, fDay

    fYear = 2015
    fMonth = 3
    fDay = 3

    if to is None or len(to.split('.')) != 3:
        return "to date is error"
    
    tYear = int(to.split('.')[0])
    tMonth = int(to.split('.')[1])
    tDay = int(to.split('.')[2])
    print "to date is:", tYear, tMonth, tDay

    if DB.client is None:
        logger.error("can not find DB")
        return "can not find DB"

    db = DB.get_db(G_DB_FUNDS)
    print db
    if db is None:
        logger.error("get database(%s) failed" % (G_DB_FUNDS))
        return "get database(%s) failed" % (G_DB_FUNDS)

    col_daily = DB.create_col(db, G_TABLE_RECORD_DAILY)
    if col_daily is None:
        logger.error("can not get collection(%s)" % G_TABLE_RECORD_DAILY)
        return "can not get collection(%s)" % G_TABLE_RECORD_DAILY

    fdFrom={G_NAME_JLRQ:datetime.datetime(fYear, fMonth, fDay)}
    pFrom = DB.find_one(col_daily, fdFrom)
    print pFrom
    print "--", type(pFrom)
    #print "--", json.

    fdTo = {G_NAME_JLRQ:datetime.datetime(tYear, tMonth, tDay)}
    pTo = DB.find_one(col_daily, fdTo)
    #print pFrom['dwjz'], pTo['dwjz'] 
    print pTo
    #return 
    fDwjz = float(pFrom['dwjz'])
    tDwjz = float(pTo['dwjz'])
    print fDwjz, tDwjz

    inc = (tDwjz - fDwjz)/ fDwjz
    print inc

    if name is None:
        cnt = 0
        for post in DB.find_all(col_daily):
            if post is not None and cnt < count:
                cnt += 1
                print post
        
    else:
        fd = {G_NAME_JJDM: name}

        print DB.find_one(col_daily, fd)
