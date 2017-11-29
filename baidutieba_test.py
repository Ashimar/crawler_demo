# coding:utf-8
"""
爬百度贴吧
https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

"""
import urllib
import urllib2
import re, sys

reload(sys)
sys.setdefaultencoding('utf-8')

class BDTB:

    def __init__(self, base_url, see_lz):
        # 是否只看楼主
        self.see_lz = "?see_lz=" + str(see_lz)
        # 基础链接
        self.base_url = base_url
        # 写入文件
        self.file = None
        # 拿到的数据
        self.datas = []

    # 获取页面编码
    def get_page_code(self, page_num):
        url = self.base_url + self.see_lz + "&" + "pn=" + str(page_num)
        print url
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            page_code = response.read().decode('utf-8')
            return page_code
        except Exception, e:
            if hasattr(e, "reason"):
                print "百度贴吧请求失败，原因：" +  e.reason
                return None

    # 处理页面编码
    def get_page_item(self, page_num):
        page_code = self.get_page_code(page_num)
        # 获取贴吧标题
        title_sel = '<div.*?<h3.*?">(.*?)</h3>'
        title_pattern = re.compile(title_sel, re.S)
        titles = re.findall(title_pattern, page_code)
        title = titles[0]
        self.setFileTitle(title)

        # 获取写入内容
        # 第一个分组是发布者，第二个分组是内容，第三个分组是楼层
        re_str = '<div.*?fr=pb" target="_blank">(.*?)</a>.*?<div id="post_content.*?">(.*?)</div>'+\
                 '.*?<span class="tail-info">(.*?)</span>'
        pattern = re.compile(re_str, re.S)
        items = re.findall(pattern, page_code)
        for item in items:
            if len(item) >= 3:
                data_dict = {}
                data_dict["author"] = item[0]
                data_dict["content"] = item[1]
                data_dict["floor"] = item[2]
                self.datas.append(data_dict)

        self.write_data()


    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def write_data(self):
        # 向文件写入每一楼的信息
        for item in self.datas:
            floor = u'----%s 层----来自： %s-----\n' % (item['floor'], item['author'])

            self.file.write(floor)
            self.file.write(item["content"] + '\n\n')

bdtb = BDTB(base_url="https://tieba.baidu.com/p/3138733512", see_lz=1)
bdtb.get_page_item(1)