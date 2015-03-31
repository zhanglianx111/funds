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

    if name is None:
        cnt = 0
        for post in DB.find_all(col_daily):
            if post is not None and cnt < count:
                cnt += 1
                print post
        
    else:
        fd = {G_NAME_JJDM: name}

        print DB.find_one(col_daily, fd)
