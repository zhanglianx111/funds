#!/usr/bin/env python
# coding=utf-8
import re
import json
import urllib2
import logging

logger = logging.getLogger(__name__)


def get_original_data(url):
    if url == "":
        logger.error("funds server url is None")
        return None

    try:
        respone = urllib2.urlopen(url)
    except urllib2.URLError():
        logger.error("connect funds server failed")
        return None

    return respone


def get_jijin_data(respone):
    if respone is None:
        return None

    data = respone.read()
    if data == "":
        logger.error("read funds data from respone failed")
        return None

    ret = data.split('=', 2)[1]
    if ret != "":
        logger.debug("funds data:%s" % ret)
        return ret
    else:
        logger.error("get funds data failed")
        return None


def add_sing_quotes(funds_data):
    if funds_data is None:
        return None

    data = re.sub(r"(\s?)(\w+):", r"'\2':", funds_data)
    if data != "":
        logger.debug("add sing quotes OK")
        return data
    else:
        logger.error("add sing quotes failed")
        return None


def del_indexsy_data(funds_data):
    if funds_data is None:
        return None

    data = re.sub(r"(\d+\.\d+,)", r"", funds_data)
    if data != "":
        logger.debug("delete indexsy's data OK")
        return data
    else:
        logger.error("delete indexsy's data failed")
        return None


def replace_sing_quotes(funds_data):
    if funds_data is None:
        return None

    data = funds_data.replace("'", "\"")
    if data != "":
        logger.debug("replace sing quotes OK")
        return data
    else:
        logging.debug("replace sing quotes failed")
        return None


def get_datas(funds_data):
    if funds_data is None:
        return None

    data = funds_data['datas']
    if data != "":
        logger.debug("convert json data OK")
        return data
    else:
        logger.error("convert json data failed")
        return None

def json_datas(datas):
    if datas == None:
        logger.error("datas is None")
        return None

    jdatas = json.loads(datas)
    if jdatas != "":
        logger.debug("convert json data OK")
        return jdatas
    else:
        logger.error("connect json data failed")
        return None
