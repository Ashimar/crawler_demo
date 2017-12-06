# coding:utf-8

# import requests
#
# target_url = 'http://quote.stockstar.com/stock'
#
# proxy_ip = {
#     'http': '183.144.200.226:28807',
#     'https': '180.118.243.242:61234',
#
# }
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
#
# proxy_support = requests.get(target_url, proxies=proxy_ip, headers=headers)
# print proxy_support.status_code
# print proxy_support.text
#

import urllib
url = "http://quote.stockstar.com/stock"  #打算抓取内容的网页
proxy_ip={'http': '27.17.32.142:80'}  #想验证的代理IP
proxy_support = urllib.request.ProxyHandler(proxy_ip)
opener = urllib.Request.build_opener(proxy_support)
opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
urllib.Request.install_opener(opener)
print(urllib.Request.urlopen(url).read())