#coding=utf8
import MySQLdb
import os
#os.startfile('myfile.py')

con = MySQLdb.connect(host='45.78.57.254', user='', passwd='', db='poem')

cursor = con.cursor()

sql = "select * from pluralpoem"

cursor.execute(sql)

row = cursor.fetchone()
rows = cursor.fetchall()
for i in rows:
    print "list::", i
print row

cursor.close()

con.close()

# #coding=utf8
# __author__ = 'changdongsheng'
#
# import datetime
# import sqlalchemy as SA
# from sqlalchemy.orm import object_session
# from sqlalchemy.ext.declarative import declarative_base
# from furion.config import settings
#
#
# class tBase(object):
#     session = property(lambda self: object_session(self)) #记录已有的session,hold住一个数据传输通道
#
#     create_date = SA.Column(SA.DateTime, default=datetime.datetime.now)
#     modified_date = SA.Column(SA.DateTime, default=datetime.datetime.now, onupdate=SA.text("current_timestamp"))
#
#
# machine_no = None
#
#
# Base = declarative_base(cls=tBase)
#
#
# echo = settings.echo_sql
# db_info = settings.db
#
# db = SA.create_engine(
#     "mysql://%s:%s@%s/%s?charset=utf8" % (db_info["user"], db_info["password"], db_info["host"], db_info["db_name"]),
#     echo=echo,
#     pool_recycle=3600,
#     pool_size=30,
#     max_overflow=60
# )

