# coding:utf-8

import requests

login_url = 'https://www.zhihu.com/?next=%2Fsettings%2Fprofile#signin'
headers =
r = requests.get(login_url)
print r.status_code
print r.text

# token =


payload = {
    'account':'15220874104',
    'password':'zhihuZHZ',
    # '_xsrf':

}