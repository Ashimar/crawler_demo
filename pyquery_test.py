# coding:utf-8
from pyquery import PyQuery as pq
from lxml import etree

doc = pq("<html></html>")
print doc

doc = pq(etree.fromstring("<html></html>"))
print doc

doc = pq('http://www.baidu.com')
print doc
print '------  --------'
doc = pq(filename='hello.html')
print doc.html()
print type(doc)
li = doc('li')
print type(li)

# for li in lis.items():
#     print li.html()
#
# print lis.each(lambda e: e)


