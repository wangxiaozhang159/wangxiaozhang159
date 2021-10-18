
import requests
from lxml import etree
import datetime
import time
import yagmail
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
}

# 获取网站源码
def get_text(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text

def cj():#采集目录页面里面文章的url
    tit_urls = 'http://mrxwlb.com/2021/10/'
    html = etree.HTML(get_text(tit_urls, headers))
    wz_url_list = html.xpath('//p[@class ="read-more"]/a/@href')
    #name_list = html.xpath('//section[@class="entry-content"]/p/strong/text()')
    # now = datetime.datetime.now()
    # jieguo = dict(zip(name_list, wz_url_list))
    jieguo = list(wz_url_list)
    #print(jieguo)
    return jieguo

def zw_():
    tit_urls=cj()
    for tit_urls in tit_urls:
        # tit_urls=tit_urls.text()
        html = etree.HTML(get_text(tit_urls, headers))
        #wz_url_list = html.xpath('//h1[@class="entry-title"]/text()')
        #wz_url_list = html.xpath('//time[@class="entry-date"]@datetime')
        #wz_url_list = html.xpath('//section[@class ="entry-content"]//li/text()')
        ####爬取正文中的小标题
        #wz_url_list = html.xpath('//section[@class ="entry-content"]/p/strong/text()')#爬取正文中的小标题
        # ##爬取正文
        name_list = html.xpath('//section[@class="entry-content"]//p/text()')   #正文采集的问题是：有的正文分三段，但标题只有一个，怎么合并
        ####wz_url_list = html.xpath('//strong[./text()=""]/following::text()')
        ##wz2_url_list = html.xpath('//section[@class ="entry-content"]//li/text()')
        ##wz_url_list.append(wz2_url_list)

        # now = datetime.datetime.now()
        # jieguo = dict(zip(name_list, wz_url_list))
        jieguo = name_list
        print(jieguo)
        print('----------------------------------------------------------------------')
    #     # return jieguo

a=[zw_()]
print(type(a))
