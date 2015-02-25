#!/usr/bin/env python

import setting
import utils
import log
import sys
from db import DB

logger = log.getMyLogger(__name__)

db_funds = DB.get_db(setting.G_DB_FUNDS)
if db_funds is None:
    logger.error("get database(%s) failed" % (setting.G_DB_FUNDS))
    sys.exit(1)

db_funds_table_index = DB.create_col(db_funds, setting.G_TABLE_FUNDS_INDEX)
if db_funds_table_index is None:
    logger.error(
        "get collection col[%s] of db[%s] failed" %
        (setting.G_TABLE_FUNDS_INDEX, setting.G_DB_FUNDS))
    sys.exit(2)

url = setting.G_URL + setting.G_TOTAL + setting.G_OTHERS
respone = utils.get_original_data(url)
d0 = utils.get_jijin_data(respone)
d1 = utils.add_sing_quotes(d0)
d2 = utils.replace_sing_quotes(d1)
d3 = utils.del_indexsy_data(d2)
jdatas = utils.json_datas(d3)
lists = utils.get_datas(jdatas)
xh = 0
for list in lists:
    jjdm = list[setting.G_JJDM]
    jjmz = list[setting.G_JJMZ]
    dwjz = list[setting.G_DWJZ]
    sgzt = list[setting.G_SGZT]
    xh = xh + 1
    # print "xh:%.4d\t\tjjdm:%.6s\tjjmz:%.9s\t\tdwjz:%.6s\tsgzt:%.4s" % (xh,
    # jjdm, jjmz, dwjz, sgzt)

    d = {jjdm: jjmz}
    if DB.find_one(db_funds_table_index, d) is not None:
        continue
    DB.insert_data2col(db_funds_table_index, d)
    #logger.info("xh:%d" % (xh))

    # if xh == 40:
    #    break
print "========================"
print DB.find_one(db_funds_table_index, d)
#DB.delete_col(db_funds, db_funds_table_index)
