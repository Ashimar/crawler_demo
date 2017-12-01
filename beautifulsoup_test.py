# coding:utf-8
import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建beautifulsoup 对象
# soup = BeautifulSoup(open('index.html')) 打开文件创建对象
soup = BeautifulSoup(html)
# 格式化打印出了它的内容
print soup.prettify()
"""
四大对象种类
Tag
NavigableString
BeautifulSoup
Comment
"""

print soup.title
print soup.a
print soup.p
print type(soup.a)

print soup.name
print soup.head.name
print soup.p['class']
print soup.p.get('class')

# 修改属性
print soup.p
soup.p['class'] = "newClass"
print soup.p
# 删除属性
del soup.p["class"]
print soup.p

# 获取标签中的内容
print soup.title.string
print type(soup.title.string)

#
print type(soup.name)
print soup.name
print soup.attts
#

print soup.a
# print soup.a.string
print type(soup.a.string)
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string

print soup.head.contents[0]
print soup.head.children
print '------ 遍历文档树 ---------'
for child in soup.body.children:
    print child
print '------ 所有子孙节点 -------'
for child in soup.descendants:
    print child

print '------ 多个内容 --------'
for string in soup.strings:
    print repr(string)

print '------- 去除空格空行 ------'
for string in soup.stripped_strings:
    print repr(string)

print '------- 父节点 ------'
content = soup.head.title.string
for parent in content.parents:
    print parent.name

print '------- 兄弟节点 ------'
print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling

print '------- 全部兄弟节点 ------'
for sibling in soup.a.next_siblings:
    print repr(sibling)

print '------- 前后节点 ------'
print soup.head.next_element

print '------- 所有前后节点 ------'
for element in soup.p.next_elements:
    print repr(element)

print '------- 搜索文档树 ---------'
print soup.find_all('b')
print soup.find_all('p')


# 未完待续：http://cuiqingcai.com/1319.html
