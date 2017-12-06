# coding:utf-8
# 还没写完，登录不上去。
import requests
import re

class Lagou():

    def __init__(self):
        print '初始化'

    #
    def get_headers(self):
        headers = {
            'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        return headers


    def get_proxies(self):

        proxies = {
            'http': '49.69.167.37:47715',
        }
        return proxies

    def login(self):
        login_url = 'https://passport.lagou.com/login/login.html'

        payload = {
            'username': '996606326@qq.com',
            'password': 'zhz12123123412',
        }

        r = requests.post(login_url, headers=self.get_headers(), params=payload, proxies=self.get_proxies())

        print r.text
        print r.cookies
        print r.status_code

        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        return cookies

    def target(self):

        url = 'https://account.lagou.com/account/cuser/userInfo.html'
        cookies = self.login()

        r = requests.get(url, cookies=cookies, headers=self.get_headers(), proxies=self.get_proxies())
        print r.text


lagou = Lagou()

lagou.target()