#coding:UTF-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()
# 定义user对象


class User(Base):
    __tablename__ = 'user_first'
    # 表的结构
    id = Column(String(20), primary_key=True)
    username = Column(String(20))


class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# 初始化数据库连接
# db = SA.create_engine(
#     "mysql://%s:%s@%s/%s?charset=utf8" % (db_info["user"], db_info["password"], db_info["host"], db_info["db_name"]),
engine = create_engine("mysql://%s:%s@%s/%s" % ("root", "1111", "localhost", "test"))
#  engine = create_engine('mysql://root:1111@localhost/test')
# 创建DBsession类型：
DBSession = sessionmaker(bind=engine)

#创建session
session = DBSession()
#创建Query查询，filter是where查询条件，最后调用one()返回唯一行，如果调用all()就返回所有行
user = session.query(User).filter(User.id == 9).one()
# @staticmethod
#     def verify_mobile(mobile):
#         with sessionCM() as session:
#             result = session.query(User).filter(User.mobile == mobile).first()
#             if result:
#                 return {"status": "error", "error_code": error_code.get("has_existed"), "message": "此电话号码已经注册"}
#             else:
#                 return {"status": "success", "msg": "可以注册"}
auser = session.query(User).filter().all()
#打印类型和对象的name属性
print 'type==', type(user), ",username:", user.username
for i in auser:
    print i.id, "username:", i.username
#关闭session
session.close()

# class User(Base):
#     __tablename__ =  'user'
#     #表的结构
#     id = Column(String(20), primary_key=True)
#     username = Column(String(20))
#     books = relationship('Book')
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', username='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()




