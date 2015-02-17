#!/usr/bin/env python

import setting
import utils

'''
respone = urllib2.urlopen(setting.G_URL)
tmpdata = respone.read()
d0 = tmpdata.split('=', 2)[1]

d1 = re.sub(r"(\s?)(\w+):", r"'\2':", d0)
d2 = d1.replace("'", "\"")
data = re.sub(r"(\d+\.\d+,)+", r"", d2)
jdata = json.loads(data)
lists = jdata['datas']
'''
url = setting.G_URL + setting.G_NUMBER + setting.G_OTHERS
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
    print "xh:%.4d\t\tjjdm:%.6s\tjjmz:%.9s\t\tdwjz:%.6s\tsgzt:%.4s" % (xh, jjdm, jjmz, dwjz, sgzt)
    if xh == 40:
        break

