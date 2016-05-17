#coding=utf-8
from urllib2 import Request,urlopen,URLError,HTTPError
req =Request("http://my.csdn.net/wxg694175346")
try:
    response = urlopen(req)
except URLError,e:
    if hasattr(e,"code"):
        print "the secver couldn\'t fulfill the request."
        print "Code::",e.reason
    elif hasattr(e,"reason"):
        print "we failed to reach a sever."
        print "Reason:",e.reason
else:
    print "No exception was catched."