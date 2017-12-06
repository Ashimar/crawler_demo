# coding:utf-8

import requests, urllib2, re


def get_imgCode(img_url):
    # 验证码的处理#
    # 验证码生成页面的地址#
    im_url = img_url
    # 读取验证码图片#
    im_data = urllib2.urlopen(im_url).read()
    # 打开一个Code.PNG文件在D盘，没有的话自动生成#
    f = open('Code.png', 'wb')
    # 写入图片内容#
    f.write(im_data)
    # 关闭文件#
    f.close()

def login_factoryhelper():
    # post提交地址，用chrome浏览器的开发者工具监控得到
    #  方法一： 使用 requests 实现
    loginurl = 'http://www.zcf8.com/login'
    mysite = 'https://i.taobao.com/my_taobao.htm?spm=a1z08.2.1997525045.1.1cbcff19ekOAhi&nekot=YXNoaW1hcl/W6Q==1512061257202'

    img_response = requests.get(loginurl)
    contents = img_response.text
    img_pattern = re.compile('<div class="tu-yz posr">.*?<img src="(.*?)"', re.S)
    img_msg = re.findall(img_pattern, contents)
    img_url = img_msg[0]
    get_imgCode(img_url)
    img_code = raw_input(u'请输入验证码：')

    data = {
        "phone_num": "15220874104",
        "password": u"1234567",
        "imgcode": img_code,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    cookies = {
    'Cookie':'BAIDUID=8B6FD303B57ABD2673F20AAB6C0010F9:FG=1; BIDUPSID=8B6FD303B57ABD2673F20AAB6C0010F9; PSTM=1487129579; HMACCOUNT=39703B97453094B8; MCITY=-119%3A; BDUSS=k1UNjJXTk1PZHVQWUlyYk9mMDZkR3A4cGlpV1h6RlhpNkJsVXdTSlJkRXBTZ3hhTVFBQUFBJCQAAAAAAAAAAAEAAACq139y0N7T8dGpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACm95FkpveRZe; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=6; H_PS_PSSID=1439_24886_18194_21091_17001_20691_25178_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
    }
    # 请求登录接口
    r = requests.options(loginurl, params=data, headers=headers, cookies=cookies)
    print r.status_code

    # 将CookieJar转为字典：
    # cookies = requests.utils.dict_from_cookiejar(r.cookies)
    # # 请求我的淘宝界面
    # r = requests.get(mysite, cookies=cookies, headers=headers )
    print r.text

login_factoryhelper()