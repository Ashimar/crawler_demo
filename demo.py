# coding:utf-8
import urllib
import urllib2
"""
urlopen(url, data, timeout)
第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
"""
# response = urllib2.urlopen("https://www.baidu.com/")
#
# print response.read()
#
print '---- 使用 request -----'
# request = urllib2.Request("https://www.baidu.com/")
# response = urllib2.urlopen(request)
# print response.read()
#
print '------ POST 登录 -------'
# values = {"username": "996606326@qq.com", "password": "zhz12123123412"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()
#
print '--------GET ---------'
# values = {}
# values['username'] = "996606326@qq.com"
# values['password'] = "zhz12123123412"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()

print '添加header'
# values = {}
# values['username'] = "15220874104"
# values['password'] = "zhihuZHZ"
# url = "https://www.zhihu.com/?next=%2Fsettings%2Faccount#signin"
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)"
# headers = {'User-Agent': user_agent}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# page = response.red()
# print page

print '------- URLError ----------'
# request = urllib2.Request('http://www.xxxassdf.com')
#
# try:
#     response = urllib2.urlopen(request)
#     print response.read()
# except urllib2.URLError, e:
#     print e.reason

print '--------- HTTPError ------------'
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    if e.hasattr('reason'):
        print e.reason


