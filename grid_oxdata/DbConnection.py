# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import xlab.local_settings as settings
from django.db import connection, transaction, connections


class DBConnection(object):

    """docstring for DbConnection"""

    def connect(self):
        dbhost = settings.OXDATA_DATA_HOST
        dbuser = settings.OXDATA_DATA_USERNAME
        dbpass = settings.OXDATA_DATA_USERPASS
        dbname = settings.OXDATA_DATA_DBNAME
        try:
            con = mdb.connect(dbhost, dbuser, dbpass, dbname)
            cur = con.cursor()
            return cur
        except mdb.Error, e:
            sys.exit(1)


class DjangoDbConnection(object):

    """docstring for DjangoDbConnection"""

    def __init__(self, dbname='default'):
        self.cursor = connections[dbname].cursor()
        self.dbname = dbname

    def fetchvalue(self, tablename):
        sqlstr = "SELECT * from %s" % (tablename)
        self.cursor.execute("SELECT * from %s" % (tablename))
        return self.cursor.fetchall()

    def get_account_history(self, userid):
        sqlstr = "select SourceAccount, DestinationAccount, TransactionAmount,\
         Description from TransactionData where DestinationAccount='%s'"\
          % (userid)
        self.cursor.execute(sqlstr)
        return self.cursor.fetchall()

    def insert_data(self, query):
        self.cursor.execute(query)

    def commit_transaction(self):
        transaction.commit_unless_managed(using=self.dbname)

    def dictfetchall(self, cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
