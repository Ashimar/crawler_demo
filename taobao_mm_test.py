# coding:utf-8

"""
抓取淘宝MM信息
 http://mm.taobao.com/json/request_top_list.htm?page=1，
1.抓取淘宝MM的姓名，头像，年龄

2.抓取每一个MM的资料简介以及写真图片

3.把每一个MM的写真图片按照文件夹保存到本地

4.熟悉文件保存的过程

"""
import urllib, urllib2, re, sys, os
import tool, requests

reload(sys)
sys.setdefaultencoding('utf-8')

class TaoBaoMM:

    def __init__(self):
        self.tool = tool.Tool()
        self.url = "http://mm.taobao.com/json/request_top_list.htm" + "?page="

    def set_proxy(self, request_url):
        # proxy = urllib2.ProxyHandler({'http' : 'http://some-proxy.com:8080'})
        # opener = urllib2.build_opener(proxy)
        # urllib2.install_opener(opener)
        response = urllib2.urlopen(request_url)
        return response

    # 获取列表界面的内容
    def get_page_code(self, page_num):

        # request = urllib2.Request(self.url+str(page_num))

        # response = urllib2.urlopen(request)
        response = self.set_proxy(self.url+str(page_num))
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

    def login_taobao(self, target_url):

        # post提交地址，用chrome浏览器的开发者工具监控得到
        #  方法一： 使用 requests 实现
        loginurl = 'https://login.taobao.com/member/login.jhtml'

        data = {
            "TPL_username": "996606326@qq.com",
            "TPL_password": "zhz12123123412",
            "J_NcoToken": 'ed90a2b6485fd1608e53ea96dbcb6c63a484a76e',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }

        def get_proxies():
            proxies = {
                'http': '49.69.167.37:47715',
            }
            return proxies
        # 请求登录接口
        r = requests.post(loginurl, params=data, headers=headers, proxies=get_proxies())
        print r.status_code

        # 将CookieJar转为字典：
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        # 请求我的淘宝界面
        r = requests.get(target_url, cookies=cookies, headers=headers)
        return r.text

    # 获取MM个人详情界面
    def get_detail_page(self, info_url):
        return self.login_taobao(info_url)

    # 获取个人文字简介
    def get_brief(self, page):
        pattern = re.compile('<div class="mm-aixiu-content" id="J_ScaleImg">(.*?)<!--', re.S)
        result = re.search(pattern, page)

        return self.tool.replace(result.group(1))

    # 获取页面所有图片
    def get_all_image(self, page):
        pattern = re. compile('<div class="mm-aixiu-content(.*?)<!--', re.S)
        content = re.search(pattern, page)
        patternImg = re.compile('<img style="float: none;margin: 10.0px;" src="(.*?)"', re.S)
        images = re.findall(pattern, str(content))
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


'''还差图片保存的内容'''