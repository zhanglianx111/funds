#!/usr/bin/env python
# coding=utf-8
import logging
from setting import  G_LOG_NAME, G_LOG_DIR 

logging.basicConfig(filename = G_LOG_DIR + G_LOG_NAME, level = logging.INFO, filemode = 'a', format = '[%(asctime)s-%(levelname)s-%(module)s(%(lineno)d)] %(message)s')

def getMyLogger(name):
    logger = logging.getLogger(name)
    return logger

