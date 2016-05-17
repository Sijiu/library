# -*- coding: utf-8 -*-


import pickle, shelve


# pickle 泡菜 shelve 搁置，上架
# 二进制文件dat

# brand = ["pickle", "shelve", "text"]
# dit = {"first": "html", "second": "C", "third": "java"}
# fl = open("pickle2.dat", "wb")
# pickle.dump(brand, fl, True) #默认为 Flase 文本格式写入
# pickle.dump(dit, fl)
# fl.close()

# 反序列化
# f = open("pickle2.dat", "rb")
# brand = pickle.load(f)
# dit = pickle.load(f)
# print "brand:", brand
# print "dit:", dit
# f.close()

# s = shelve.open("pickle22.dat")
# s["brand"] = ["css", "js"]
# s["lang"] = {"first": "C", "second": "java", "third": "python"}
# s.sync()

# ss = shelve.open("pickle22.dat")
# print "shelf:", ss["brand"]
# print "shelve:", ss["lang"]
# ss.close()


# try:
#     ss = open("shelf1.dat")
# except IOError:
#     print "The file isn't exist!"
# 学会制造异常，然后获取准确的名称

assert len("love") == len("like")




