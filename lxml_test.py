# coding:utf-8
"""
pip install lxml

XPath 是一门在 XML 文档中查找信息的语言。
XPath 可用来在 XML 文档中对元素和属性进行遍历。
XPath 是 W3C XSLT 标准的主要元素，并且 XQuery 和 XPointer 都构建于 XPath 表达之上。

"""

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
# 首先我们使用 lxml 的 etree 库，然后利用 etree.HTML 初始化，然后我们将其打印出来。
result = etree.tostring(html)
print result
"""
其中，这里体现了 lxml 的一个非常实用的功能就是自动修正 html 代码，大家应该注意到了，最后一个 li 标签，
其实我把尾标签删掉了，是不闭合的。不过，lxml 因为继承了 libxml2 的特性，
具有自动修正 HTML 代码的功能。
"""

html = etree.parse('hello.html')
result = etree.tostring(html, pretty_print=True)
print(result)


select_ = html.xpath('//li')
print select_
print type(select_)
print type(select_[0])

select_class = html.xpath('//li/@class')
print select_class

select_a = html.xpath('//li/a[@href="link1.html"]')
print result


# 未完待续：http://cuiqingcai.com/2621.html
