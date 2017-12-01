# coding:utf-8
import requests
"""
# 初探
url = 'http://cuiqingcai.com'
r = requests.get(url)
print r.status_code
print r.headers['content-type']
print r.encoding
# print r.text
# print r.json()
print r.cookies

# 基本请求
r = requests.post("http://httpbin.org/post")
print r.status_code
r = requests.put("http://httpbin.org/put")
print r.status_code
r = requests.delete("http://httpbin.org/delete")
print r.status_code
r = requests.head("http://httpbin.org/get")
print r.status_code
r = requests.options("http://httpbin.org/get")
print r.status_code

# ---- get
url = "http://apistore.baidu.com/microservice/weather"
payload = {"citypinyin": 'beijing'}
r = requests.get(url, params=payload)
print r.status_code
print r.text


r = requests.get('http://www.taobao.com')
print r.cookies
print r.cookies['cookie_name']

# 发送cookies 信息
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

# 超时配置
requests.get('http://github.com', timeout=0.001)
# requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='github.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x10313a210>, 'Connection to github.com timed out. (connect timeout=0.001)'))

# 会话对象
s = requests.Session()
# s.headers
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print r.text


s = requests.Session()
s.headers.update({'x-test':'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2':'true'})
print r.text
"""

# 代理
proxies = {
    "https": "http://41.118.132.69:4433"

}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text
