# coding:utf-8

"""
抓取淘宝MM信息
 http://mm.taobao.com/json/request_top_list.htm?page=1，
1.抓取淘宝MM的姓名，头像，年龄

2.抓取每一个MM的资料简介以及写真图片

3.把每一个MM的写真图片按照文件夹保存到本地

4.熟悉文件保存的过程

淘宝的登录字段
TPL_username
TPL_password

um_token:HV01PAAZ0b8d93f3790da4e75a1f5e6700441fec
ua:099#KAFEtGEBEMdE6YTLEEEEE6twScREG6PFSuJFC6Vqgc978ffFSuBED6N1SciIV6QBSyR5V6NJZXCjVISiDy1KG6V3SXJ5C1qTETiL/9iDUxZVspJLgcBKC0Oivt+O8+qTETiL/9iDpqCVspJLgcBKC0Oivt+O8gdTEEi5DEEErGFEhrclHgohluZdsR9MZFStUXcfnM9SZy89ZRp66GFE1XZVR1QwluZuSLoTEEvP/DTj0llP/mkmE7EFsyaDdRdTEEx6zIywTGFETrZtt3illW4TEHITt3qEjrjopxA4D4AkWhErokQo1+RV0HUaBFt05c6ok8j2iHfkukj2qmA3kkkZy8m4mKjxxRzbokV/k0Pllkj2qDAp1ZWcqNGt060qm/N4kLgoO7FEpcZdtcRlluZVsyaa+3llsvnP/36alllzgcZddQlllu8Xsyaa+3llW0W/E7EhssaZtfxdJ7FE1cZdt054JNKXgGFEjPilEI/qaWw7zVZBNdZ6bteWNweGL5eDZ/e0Ps0twyJoPPqVNdZ6bteWNw5SaGZQSpw5cRNE99rqUt7BbQZ6btuAvshnwBS9E7EFD67EEp5TEEi5D7EE6GFE1XZlMZKRluZdwioTEEvPrpZ/t3lP/jFnE7EKsyOCdp9lsyVbrGFEwcZWAqBHTcZdsyXGbTdTEEi5DEEEIGFEHccdt3mFGsvbUXcFVovK8Pc9Zpr2IGFEHccdt3kgkyvbUXcFVovK8Pc9Zpr2

使用的第三方 ：
> pip install lxml
"""
import urllib, urllib2, re, sys, os
import tool
from lxml import html
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

class TaoBaoMM:

    def __init__(self):
        self.tool = tool.Tool()
        self.url = "http://mm.taobao.com/json/request_top_list.htm" + "?page="

    # 获取列表界面的内容
    def get_page_code(self, page_num):

        request = urllib2.Request(self.url+str(page_num))

        response = urllib2.urlopen(request)

        page_code = response.read().decode('gbk')

        # print page_code

        return page_code

    # 处理列表界面的内容
    def get_contents(self, page_num):

        page_code = self.get_page_code(page_num)

        pattern = re.compile('<div.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class.*?"_blank">(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)

        items = re.findall(pattern, page_code)
        contents = []
        for item in items:
            if len(item) == 5:
                print '--------'
                print '个人主页 http:' + item[0]
                print '头像 http:' + item[1]
                print item[2]
                print item[3]
                print item[4]
                contents.append(['http:' + item[0], 'http:' + item[1], item[2], item[3], item[4]])
        return contents

    # 获取MM个人详情界面
    def get_detail_page(self, info_url):
        """
        获取MM个人详情界面
        这里需要登录
        :param info_url:
        :return:
        """
        # url
        login_url = 'https://login.taobao.com/member/login.jhtml'
        request = urllib2.Request(login_url)
        response = urllib2.urlopen(request)
        page_code = response.read().decode('gbk')



        #
        # target_url = info_url
        #
        # session_requests = requests.session()
        # result = session_requests.get(login_url)
        # page_code
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'
        #
        # headers = {'User_Agent': user_agent}
        # values = {
        #     "TPL_username": "ashimar_珠",
        # }
        # data = urllib.urlencode(values)
        # request = urllib2.Request(login_url, data, headers)
        # response = urllib2.urlopen(request)
        # page_code = response.read().decode('gbk')
        # pattern = re.compile('<input type="hidden" name="um_token" value="(.*?)">', re.S)
        # items = re.findall(pattern, page_code)
        #
        # um_token = items
        # payload = {
        #     "TPL_username": "ashimar_珠",
        #     "TPL_password": "zhz12123123412",
        #     "um_token": um_token,
        #
        # }
        # session_requests = requests.session()
        # result = session_requests.post(login_url, data=payload, headers=dict(referer=login_url))
        #
        # response = session_requests.get(target_url, headers=dict(referer=target_url))

        return response.read().decode('gbk')

    # 获取个人文字简介
    def get_brief(self, page):
        pattern = re.compile('<div class="<div.*？mm-aixiu-content(.*?)<!--', re.S)
        result = re.search(pattern, page)

        return self.tool.replace(result.group(1))

    # 获取页面所有图片
    def get_all_image(self, page):
        pattern = re. compile('<div class="mm-aixiu-content(.*?)<!--', re.S)
        content = re.search(pattern, page)
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(pattern, content.group(1))
        return images

    # 保存多张图片
    def save_images(self, images, name):
        number = 1
        print u'find ', name, u'total ', len(images), u'pictures'
        for image_url in images:
            split_path = image_url.split('.')
            ftail = split_path.pop()
            if len(ftail) > 3:
                ftail = "jpg"
            file_name = name + "/" + str(number) + "." + ftail
            self.save_image(image_url, file_name)
            number += 1

    # 保存图片
    def save_image(self, image_url, file_name):
        u = urllib.urlopen(image_url)
        data = u.read()
        f = open(file_name, 'wb')
        f.write(data)
        f.close()

    # 保存头像
    def save_icon(self, icon_url, name):
        split_path = icon_url.split('.')
        ftail = split_path.pop()
        file_name = name + "/icon." + ftail
        self.save_image(icon_url, file_name)

    # 保存个人简介
    def save_brief(self, content, name):
        filename = name + "/" + name + ".txt"
        f = open(filename, "w+")
        print u'正在保存', filename
        f.write(content.encode('utf-8'))

    def mkdir(self, path):
        path = path.strip()

        is_exists = os.path.exists(path)

        if not is_exists:
            os.makedirs(path)
            return True
        else:
            return False

    def save_page_info(self, page_index):
        contents = self.get_contents(page_index)
        for item in contents:
            # 个人详情页的URL
            detail_url= item[0]
            detail_page = self.get_detail_page(detail_url)
            brief = self.get_brief(detail_page)
            images = self.get_all_image(detail_page)
            self.mkdir(item[2])
            self.save_brief(brief, item[2])
            self.save_icon(item[1], item[2])
            self.save_images(images, item[2])

            # 传入起止页码，获取MM图片

    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print u"正在偷偷寻找第", i, u"个地方，看看MM们在不在"
            self.save_page_info(i)


tbmm = TaoBaoMM()
tbmm.savePagesInfo(1, 10)