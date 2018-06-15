#coding:utf-8
'''
引擎组件
     负责驱动各大组件，通过调用各自对外提供的API接口，实现它们之间的交互和协作
     提供整个框架的启动入口
'''
from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline

from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware

# 导入数据类
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

from scrapy_plus.utils.log import logger

# 导入时间模块用于记录时间
from datetime import datetime


class Engine(object):

    def __init__(self, spider):
        self.spider = spider
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        # 实例化中间件
        self.spider_mid = SpiderMiddleware()
        self.downloader_mid = DownloaderMiddleware()

    def _start_engine(self):
        # 编写引擎调度流程

        # 1调用spider模块的start_requests方法，获取起始的请求
        start_request = self.spider.start_requests()

        # ----1调用爬虫中间件的process_request方法处理请求
        start_request = self.spider_mid.process_request(start_request)

        # 2将起始的请求传递给调度器模块的add_request方法
        self.scheduler.add_request(start_request)

        # 3调用调度器模块的get_request方法，从带爬取队列中获取一个请求
        request = self.scheduler.get_request()

        # ----2调用下载器中间件类的process_request方法
        request = self.downloader_mid.process_request(request)

        # 4将获取到的请求交给下载器模块的get_response方法,获得请求对应的响应
        response = self.downloader.get_response(request)

        # ----3调用下载器中间件的process_response方法
        response  = self.downloader_mid.process_response(response)

        # 5.将响应交给spider模块的parse方法用于解析，获取解析结果
        result = self.spider.parse(response)

        # 6判断解析结果类型
        if isinstance(result, Request):
            # ----1调用爬虫中间件的process_request方法处理请求
            result = self.spider_mid.process_request(result)

            # 如果是request对象，则调用调度器模块的add_request方法，建请求放入队列
            self.scheduler.add_request(result)

        if isinstance(result, Item):
            result = self.spider_mid.process_item(result)

            # 如果是item对象，则调用pipeline模块的process_item方法处理
            self.pipeline.process_item(result)
        else:
            raise Exception('框架不支持的数据类型')

    def start(self):
        start = datetime.now()
        logger.info("引擎启动时间{}".format(start))
        self._start_engine()
        stop = datetime.now()
        logger.info("引擎停止时间{}".format(stop))
        # 需要使用total_Seconds转换成秒
        logger.info("爬虫运行时间{}".format((stop-start).total_seconds()))