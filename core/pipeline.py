#coding:utf-8
'''
 管道组件
     负责处理数据对象(Item)
'''


class Pipeline(object):

    def process_item(self, item):
        print('管道正在处理{}数据'.format(item.data))