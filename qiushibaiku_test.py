# coding:utf-8
"""
import urllib2
import urllib
import re

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page) + '/'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)"
headers = {"User-Agent": user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')
    # print content
    pattern = re.compile('<div.*?h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
    print '开始切换格式'
    items = re.findall(pattern, content)

    for item in items:
        print '-------------每日丑事'

        print item[0], item[1], '点赞：' + str(item[2])

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

"""
import urllib
import urllib2
import re, thread, time
import MySQLdb, traceback

table_name = "qsbk_hot"

#糗事百科爬虫类
class QSBK:

    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)"
        # 初始化 hearders
        self.headers = {"User-Agent": self.user_agent}
        # 存放段子的变量， 每个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False
        # 连接数据库
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="", db="QSBK", charset="utf8")

    def get_page(self, page_index):
        """
        传入某一页的引索获得页面代码
        :param page_index:
        :return:
        """
        url = 'https://www.qiushibaike.com/hot/page/' + str(page_index) + '/'
        try:
            # 构建request
            request = urllib2.Request(url, headers=self.headers)
            # 利用urlopen 获取页面代码
            response = urllib2.urlopen(request)
            # 将页面转化为utf-8编码
            page_code = response.read().decode('utf-8')
            print '----------------'
            print type(page_code)
            return page_code
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None

    # 传入某一页代码，返回本页不带图片的段子列表
    def get_page_items(self, page_index):
        page_code = self.get_page(page_index)
        if not page_code:
            print "页面加载失败……"
            return None
        pattern = re.compile('<div.*?h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, page_code)
        # 用来存储每页的段子们
        page_stories = []
        # 遍历正则表达式匹配信息
        for item in items:
            # item[0] 是发布者， item[1] 是发布内容 item[2] 是点赞数
            page_stories.append([item[0], item[1],item[2]])

        return page_stories

    # 加载并提取页面的内容， 加入到列表中
    def load_page(self):
        # 如果当前未查看页数少于2页，则加载新一页
        if self.enable is True:
            if len(self.stories) < 2:
                # 获取新一页
                page_stories = self.get_page_items(self.pageIndex)
                # 将该页的段子存放到全局list中
                if page_stories:
                    self.stories.append(page_stories)
                    # 获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def get_one_story(self, page_stories, page):
        # 遍历一页的段子
        for story in page_stories:
            # 等待用户输入
            input = raw_input()
            # 每当输入回车一次， 判断一下是否要加载新页面
            self.load_page()
            # 如果输入Q则程序结束
            if input == "Q" or input == 'q':
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t发布时间：%s\t赞：%s" % (page, story[0], story[1], story[2])
            self.save_sql(story)

    # 将拿到的数据保存到本地数据库
    def save_sql(self, story):
        print '插入数据库'

        author = story[0].strip().encode('utf-8')
        content = story[1].strip().encode('utf-8')
        like_num = story[2].strip().encode('utf-8')

        if self.check_same_data_in_sql(content) is False:
            print "存在相同的数据，不插入"
            return

        # 使用游标
        cursor = self.db.cursor()
        try:
            sql = "insert into " + table_name
            sql += "(author, content, like_num) values('%s', '%s', '%s')" % (author, content, like_num)
            print sql
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print e.reason
            traceback.print_exc()

        cursor.close()

    def check_same_data_in_sql(self, content):
        cursor = self.db.cursor()

        sql = "select * from  " + table_name
        sql += " where content='%s'" % content
        cursor.execute(sql)
        if cursor.rowcount > 0:
            cursor.close()
            return False
        cursor.close()
        return True


    # 开始执行
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q或q退出"
        # 使变量为True, 程序可以正常运行
        self.enable = True
        # 限价在一页内容
        self.load_page()
        # 局部变量，控制当前读到了第几页
        now_page = 0

        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                page_stories = self.stories[0]
                # 当前读到的页数加一
                now_page += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.get_one_story(page_stories, now_page)


qsbk = QSBK()
qsbk.start()
