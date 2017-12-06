# coding:utf-8

import urllib, urllib2, cookielib, time
import requests

# post提交地址，用chrome浏览器的开发者工具监控得到
#  方法一： 使用 requests 实现
loginurl = 'https://login.taobao.com/member/login.jhtml'
mysite = 'https://i.taobao.com/my_taobao.htm?spm=a1z08.2.1997525045.1.1cbcff19ekOAhi&nekot=YXNoaW1hcl/W6Q==1512061257202'

data = {
    "TPL_username": "996606326@qq.com",
    "TPL_password": "zhz12123123412",
    "J_NcoToken": 'ed90a2b6485fd1608e53ea96dbcb6c63a484a76e',

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}
# 请求登录接口
r = requests.post(loginurl, params=data,  headers=headers)
print r.status_code

# 将CookieJar转为字典：
cookies = requests.utils.dict_from_cookiejar(r.cookies)
# 请求我的淘宝界面
r = requests.get(mysite, cookies=cookies, headers=headers )
print r.text

#  方法二： 使用 urllib2 库实现
'''
loginurl = 'https://login.taobao.com/member/login.jhtml'
mysite = 'https://i.taobao.com/my_taobao.htm?spm=a1z08.2.1997525045.1.1cbcff19ekOAhi&nekot=YXNoaW1hcl/W6Q==1512061257202'

data = {
    "TPL_username": "996606326@qq.com",
    "TPL_password": "zhz12123123412",
    "J_NcoToken": 'ed90a2b6485fd1608e53ea96dbcb6c63a484a76e',

}
data = urllib.urlencode(data)

# 实例化一个cookies保存器
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 添加网页头将爬虫伪装成浏览器，以防止网站防采集。
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')]
# 打开登录页登录
opener.open(loginurl, data)
# 如果登录成功，就可以看到cookies了
print cj
# 登陆后可以直接打开需要登录才能访问的网页
op = opener.open(mysite)
result = op.read()

print result


# 把访问内容保存到本地网页中查看是否成功登录。
f = open('taobao.html','w')
f.writelines(result)
f.close()

'''

