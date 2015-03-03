#!/usr/bin/env python
# coding=utf-8

import utils
import log
import sys
import datetime
from database import DB
from setting import *

logger = log.getMyLogger(__name__)

if __name__ == '__main__':
    if DB.client is None:
        logger.error("can not find DB")
        sys.exit(1)

    db_funds = DB.get_db(G_DB_FUNDS)
    if db_funds is None:
        logger.error("get database(%s) failed" % (G_DB_FUNDS))
        sys.exit(2)

    '''
    创建 基金代码和基金名字 表
    '''
    db_funds_table_index = DB.create_col(db_funds, G_TABLE_FUNDS_INDEX)
    if db_funds_table_index is None:
        logger.error(
            "get collection col[%s] of db[%s] failed" %
            (setting.G_TABLE_FUNDS_INDEX, G_DB_FUNDS))
        sys.exit(3)

    '''
    创建记录 每日基金净值 表
    '''
    db_funds_table_daily = DB.create_col(db_funds, G_TABLE_RECORD_DAILY)
    if db_funds_table_daily is None:
        logger.error(
            "get collection col[%s] of db[%s] failed" %
            (setting.G_TABLE_RECORD_DAILY, G_DB_FUNDS))
        sys.exit(4)

    url = G_URL + G_TOTAL + G_OTHERS
    respone = utils.get_original_data(url)
    d0 = utils.get_jijin_data(respone)
    d1 = utils.add_sing_quotes(d0)
    d2 = utils.replace_sing_quotes(d1)
    d3 = utils.del_indexsy_data(d2)
    jdatas = utils.json_datas(d3)
    lists = utils.get_datas(jdatas)
    xh = 0
    for list in lists:
        jjdm = list[G_JJDM]
        jjmz = list[G_JJMZ]
        dwjz = list[G_DWJZ]
        sgzt = list[G_SGZT]
        xh = xh + 1
        # print "xh:%.4d\t\tjjdm:%.6s\tjjmz:%.9s\t\tdwjz:%.6s\tsgzt:%.4s" % (xh,
        # jjdm, jjmz, dwjz, sgzt)

        # 更新 index 表
        index = {G_NAME_JJDM: jjdm, G_NAME_JJMZ: jjmz}
        if DB.find_one(db_funds_table_index, index) is None:
            DB.insert_data2col(db_funds_table_index, index)

        # 将每日的基金净值记录在daily表中
        daily = {
            G_NAME_JJDM: jjdm,
            G_NAME_DWJZ: dwjz,
            # setting.G_NAME_JLRQ: datetime.date.today()}
            G_NAME_JLRQ: datetime.datetime(G_YEAR, G_MONTH, G_DAY)}

        DB.insert_data2col(db_funds_table_daily, daily)
        #print daily

    print "========================"
    #fd = {'key': jjdm}
    fd = {G_NAME_JJDM: jjdm}
    print DB.find_one(db_funds_table_index, fd)
    #DB.delete_col(db_funds, db_funds_table_index)
