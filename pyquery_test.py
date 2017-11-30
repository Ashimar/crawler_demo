# coding:utf-8
from pyquery import PyQuery as pq

doc = pq(filename='hello.html')
lis = doc('li')
for li in lis.items():
    print li.html()

print lis.each(lambda e: e)


