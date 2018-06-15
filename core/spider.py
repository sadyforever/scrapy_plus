#coding:utf-8
'''
 爬虫组件
     构建请求信息(初始的)，也就是生成请求对象(Request)
     解析响应对象，返回数据对象(Item)或者新的请求对象(Request)
'''
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

class Spider(object):

    start_url = ''

    # 将起始的url构建成请求返回
    def start_requests(self):

        return Request(self.start_url)

    def parse(self, response):

        return Item(response.url)