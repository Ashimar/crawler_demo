# coding:utf-8
import urllib2
import urllib
import cookielib
# 声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value


print '--------- 保存Cookie 到文件  ----------'
# 设置保存cookie的文件， 同级目录下的cookie.txt
# filename = 'cookie.txt'
#
# cookie = cookielib.MozillaCookieJar(filename)
#
# handler = urllib2.HTTPCookieProcessor(cookie)
#
# opener = urllib2.build_opener(handler)
#
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

print '----------- 从文件中获取Cookie并访问 ---------------'
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()

print '--------- 利用cookie模拟网站登录 没写完-----------'
# filename = 'cookie.txt'
# # 声明
# cookie = cookie.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#     'username': '15220874104'
#     'password': '1234567'
# })
# loginUrl = ''
