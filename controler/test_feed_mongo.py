# -*- coding: utf-8 -*-

from feed_mongo import Feed
import uuid
if __name__ == "__main__":
    product = {
        "name": "tom",
        "list": {
            "one": "python",
            "two": "pip"
        },
        "upc": ["isbn", "EAN"]
    }
    print "product:", product
    # feed = Feed("product_test").save(product)
    # print "feed:", feed
    # a = uuid.uuid4()
    # print "a=", a
    # print a.hex
    # f = lambda a, b, c: a+b+c
    # print "lambda=", f(1, 2, 3)
    #
    # L = [lambda x: x+2, lambda x: x*2, lambda x: x**2]
    # print "L=", L[0](1), L[1](2), L[2](3)
    # D = {"d1": lambda x: x**1,
    #      "d2": lambda x: x**2,
    #      "d3": lambda x: x**3
    #      }
    # print "D=", D["d1"](2), D["d2"](2), D["d3"](2)

    # l = lambda: lambda x: x + 5
    # b = l()
    # print "b=", b(2)
    # print "==", (l())(2)

    def inc(x):
        return x + 10
    l = [1, 2, 3]
    print map(inc, l)
    print map(lambda x: x+10, l)

