#!/usr/bin/env python
# coding=utf-8

import pymongo
import logging

import setting

logger = logging.getLogger(__name__)


class Mongodb(object):

    def __init__(self,
                 db_host,
                 db_port,
                 db_user = None,
                 db_passwd = None):

        self.host = db_host
        self.port = db_port
        self.user = db_user
        self.passwd = db_passwd
        self.client = None

    def connection(self):
        if not self.conn:
            self.conn = pymongo.MongoClient(self.host, self.port)

        # TODO add user and password authrizion

        return self.client

    def get_db(self, db_name):
        try:
            return self.client.db_name
        except InvalidName:
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
        return self.database_name()

    def create_col(self, db, col_name):
        return db.col_name

    def delete_col(self, db, col_name):
        pass

    def get_db_collection(self, db, collection):
        return db.collection_names()

    def insert_data2col(self, col_name, data):
        return col_name.insert(data)

    def find_one(self, col_name, key):
        return col_name.find_one(key)

    def find_all(self, col_name):
        return col_name.find()
