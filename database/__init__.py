#!/usr/bin/env python
# coding=utf-8

import pymongo
import log
import setting

logger = log.getMyLogger(__name__)


class Mongodb(object):

    def __init__(self,
                 db_host,
                 db_port,
                 db_user=None,
                 db_passwd=None):

        self.host = db_host
        self.port = db_port
        self.user = db_user
        self.passwd = db_passwd
        self.client = None
        if self.client is None:
            try:
                self.client = pymongo.MongoClient(self.host, self.port)
            except pymongo.errors.ConnectionFailure, e:
                logger.error(
                    "connect Mongodb[%s:%d] failed, error:%s" %
                    (self.host, self.port, e))
                return None

        # TODO add user and password authrizion

    def get_db(self, db_name):
        try:
            return self.client[db_name]
        except pymongo.errors.InvalidName:
            logger.error("Invalid database name:%s" % db_name)
            return None

    def get_db_server_host(self):
        if self.host is None:
            logger.error("Can not get Mongodb server host")
            return None

        return self.host

    def get_db_server_port(self):
        if self.port is None:
            logger.error("Can not get Mongodb server port")
            return None

        return self.port

    def list_nodes(self):
        return self.client.nodes

    ''''
    def lock(self):
        self.client.is_locked

    def unlock(self):
        self.client.unlock
    '''

    def list_databases(self):
        return self.client.database_name()

    def create_col(self, db, col_name):
        return db[col_name]

    def delete_col(self, db, col_name):
        db.drop_collection(col_name)

    def list_db_collection(self, db, collection):
        return db.collection_names()

    def insert_data2col(self, col_name, data):
        return col_name.insert(data)

    def find_one(self, col_name, key):
        return col_name.find_one(key)

    def document_count(self, col_name):
        return col_name.count()

    def find_all(self, col_name):
        return col_name.find()

DB = Mongodb(setting.G_HOST, setting.G_PORT)
