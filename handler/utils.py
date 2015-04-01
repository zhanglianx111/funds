#!/usr/bin/env python
# coding=utf-8

import time
import datetime
from setting import TIME

def IsNowTime(time):
    '''IsNowTime
    参数：
        time：datetime格式的时间
    功能：
        time和给定的时间（全局的一个时间点，在setting中定义）转化为时间戳。比较两者的时间戳，如果为负则认为传入的时间在给定的时间点之前；如果为正则认为在给定的时间之后。
    '''
    t1 = time.mktime(strptime(datetime.datetime.strptime(time)))
    t2 = time.mktime(strptime(TIME))
    
    return t1 - t2

