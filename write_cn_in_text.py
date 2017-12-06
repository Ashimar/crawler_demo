# coding:utf-8
import codecs

list = [[1,2],[3,4], [u'哈哈', 'lili']]

s = u'亚像素精度：\r\n'  #u表示读取中文，\r\n为换行符
contry = u'国家'
arr = [
    {'国家': 'Cn', 'host': '28807', 'IP': '183.144.200.226'},
    {'country': 'Cn', 'host': '61234', 'IP': '180.118.243.242'},
    {'country': 'Cn', 'host': '53281', 'IP': '125.46.0.62'},
    {'country': 'Cn', 'host': '9999', 'IP': '113.89.52.86'},
    {'country': 'Cn', 'host': '9797', 'IP': '180.173.69.27'},
    {'country': 'Cn', 'host': '9999', 'IP': '182.121.206.140'},
    ]

f = codecs.open("main.txt",'w','utf-8')
f.write(s)
#f.write(str(list))
for i in list:
    f.write(str(i)+'\r\n')  #\r\n为换行符

f.close()
