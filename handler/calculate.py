#!/usr/bin/env python
# coding=utf-8

from database import DB
import log
from setting import *

logger = log.getMyLogger(__name__)

def handler_calc(name, frm, to, sort):
    if DB.client is None:
        logger.error("can not find DB")
        return "can not find DB"

    db = DB.get_db(G_DB_FUNDS)
    if db is None:
        logger.error("get database(%s) failed" % (G_DB_FUNDS))
        return "get database(%s) failed" % (G_DB_FUNDS)

    
    col_daily = DB.get_db_collection(db.G_TABLE_RECORD_DAILY)
    if col_daily is None:
        logger.error("can not get collection(%s)" % G_TABLE_RECORD_DAILY)
        return "can not get collection(%s)" % G_TABLE_RECORD_DAILY

    fd = {G_NAME_JJMZ:name}
    print DB.find_one(col_daily, fd)


