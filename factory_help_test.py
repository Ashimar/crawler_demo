# coding:utf-8

# from pyquery import PyQuery as pq
from lxml import etree
import urllib2, re
import requests

url = 'http://www.zcf8.com/login'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page_code = response.read().decode('utf8')
pattern = re.compile('<div class="tu-yz posr">.*?<img src="(.*?)"', re.S)
items = re.findall(pattern, page_code)
print items
# ----- 获取验证码: 先把验证码保存到本地，然后输入验证码进行操作
# 验证码的处理#
# 验证码生成页面的地址#
im_url = items[0]
#读取验证码图片#
im_data = urllib2.urlopen(im_url).read()
# 打开一个Code.PNG文件在D盘，没有的话自动生成#
f=open('code.png','wb')
# 写入图片内容#
f.write(im_data)
# 关闭文件#
f.close()

imgCode = raw_input('输入验证码：')

payload = {
    "phone_num": '15220874104',
    'password': '1234567',
    'imgcode': imgCode,
    'login_mode':'1'
}
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'telhao=; keys=; PHPSESSID=90c4764e985d605c8861d6197c513acc; XSRF-TOKEN=eyJpdiI6IlV6TkkxN2drZGtUam9sZDhLd0pWbWc9PSIsInZhbHVlIjoiQjNkM0JqU3QwWEFFTzlxNWg0endKdElJdnlMZTcxaDJLZGc3VmNLeUFPNG9UZ3A3WGlYcThYWHNXbEVxN1B3VlFBV3hraWY0czF2bEk3XC9VM2pcL0pDQT09IiwibWFjIjoiZTIzOWQ5OWQ0Mjk5ZTIwMGVmYjEwMzgzNTgyZTFkZTlkNWE5YTRiMmQwMzdlZTAwMTI1NzQyZjZhNzhkODEzMiJ9; laravel_session=eyJpdiI6InZIajVOWEkrbjRsQUdCNDRIZmhjN3c9PSIsInZhbHVlIjoiNGR4c1NYS3RkaVhTRVY3NFdWR3J5TVJHSVdZRnZcLzBDa20rdmRwandURlBHaFNBNHpXang4TkRHakQzZUxpUnpsT2VPZXJoWEFTdUxqQlFnZGtTUE5BPT0iLCJtYWMiOiI1ZmQwMTQwMGY0MDVkMTNkODgyMzQwOTZiNDQ4NzYyZTg1NTZjOThlMDJjMTgyNjFlZmExZTg1MTk2MDVmMDc5In0%3D; Hm_lvt_3baf884227b4c5050c4d14b747ed52ba=1511745764,1511834840,1512013051,1512032796; Hm_lpvt_3baf884227b4c5050c4d14b747ed52ba=1512032809',
    'Host': 'www.zcf8.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',

    'X-XSRF-TOKEN': ,
}

r = requests.post(url, params=payload, headers=headers)
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text

# print response.statecode
