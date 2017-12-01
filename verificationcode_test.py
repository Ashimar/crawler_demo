# -*- coding: utf-8 -*-
import urllib2
#验证码的处理#
#验证码生成页面的地址#
im_url = 'http://www.zcf8.com/cfb/1.0.0/qrcode/33'
#读取验证码图片#
im_data = urllib2.urlopen(im_url).read()
#打开一个Code.PNG文件在D盘，没有的话自动生成#
f=open('code.png','wb')
#写入图片内容#
f.write(im_data)
#关闭文件#
f.close()