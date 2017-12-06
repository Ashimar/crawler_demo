# coding:utf-8
import requests
import re
import time
import random
import json
from bs4 import BeautifulSoup
import codecs

# catch proxy ip
# all page contents list
ip_totle=[]

for page in range(2, 6):

    url = 'http://www.xicidaili.com/wt/'+str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    page_code = r.text
    print '-------number ' + str(page)
    pattern = re.compile('<tr class="odd">(.*?)</tr>', re.S)
    ip_items = re.findall(pattern, page_code)
    print ip_items[0]

    for ip_item in ip_items:
        item_pattern = re.compile('<td.*?<img.*?alt="(.*?)".*?<td>(.*?)<.*?<td>(.*?)<', re.S)
        contents = re.findall(item_pattern, ip_item)
        # print contents[0] + '\t' + contents[1] + '\t' + contents[2]
        if len(contents) <=0:
            continue
        content = contents[0]
        ip_con = {
            'country': str(content[0]),
            'IP': str(content[1]),
            'host': str(content[2]),
        }
        ip_totle.append(ip_con)

    time.sleep(random.choice(range(1, 5)))


f = codecs.open('proxy_host_dic.txt', 'w', 'utf-8')
# JsonStr = json.dumps(ip_totle, ensure_ascii=False, encoding='UTF-8')
f.writelines(str(ip_totle).encode('utf-8'))
f.close()

    #                      '<tr class="odd">.*?alt="(.*?)">.*?<td>(.*?)<.*?<td>(.*?)<.*?<a.*?>(.*?)</a>
    #   </td>
    #   <td class="country">高匿</td>
    #   <td>HTTP</td>
    #   <td class="country">
    #     <div title="3.367秒" class="bar">
    #       <div class="bar_inner medium" style="width:73%">
    #
    #       </div>
    #     </div>
    #   </td>
    #   <td class="country">
    #     <div title="0.673秒" class="bar">
    #       <div class="bar_inner fast" style="width:97%">
    #
    #       </div>
    #     </div>
    #   </td>
    #
    #   <td>626天</td>
    #   <td>17-12-01 04:45</td>
    # </tr>)
"""
 <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
      <td>112.114.78.106</td>
      <td>8118</td>
      <td>
        <a href="/2017-11-28/yunnan">云南临沧</a>
      </td>
      <td class="country">高匿</td>
      <td>HTTP</td>
      <td class="country">
        <div title="1.818秒" class="bar">
          <div class="bar_inner fast" style="width:94%">
            
          </div>
        </div>
      </td>
      <td class="country">
        <div title="0.363秒" class="bar">
          <div class="bar_inner fast" style="width:97%">
            
          </div>
        </div>
      </td>
      
      <td>2小时</td>
      <td>17-11-28 22:43</td>
    
"""
