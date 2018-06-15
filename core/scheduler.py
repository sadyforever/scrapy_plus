#coding:utf-8
'''
 调度器组件
     缓存请求对象(Request)，并为下载器提供请求对象，实现请求的调度
     对请求对象进行去重判断
'''
# from queue import Queue
# six模块中的队列会自动判断是py2还是py3，自动使用相应版本的队列
from six.moves.queue import Queue


class Scheduler(object):

    def __init__(self):
        # 创建待爬取的任务队列
        self.queue = Queue()

    def add_request(self, request):
        # 在将请求放入队列之前对其做去重操作
        # filter_request返回False    if  什么什么 : 是简写 if 什么什么 == True:的简写
        if not self.filter_request():

            # 将请求添加到任务队列中
            self.queue.put(request)

    def get_request(self):
        request = self.queue.get()
        # 将提取到的待爬取请求返回
        return request

    def filter_request(self):
        # 判断请求是否在去重集合中，如果不存在则说明该请求没有做过，返回False
        return False