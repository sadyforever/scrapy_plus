#coding:utf-8
'''
下载器组件
     根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回
'''

import requests
from scrapy_plus.http.response import Response


class Downloader(object):

    def get_response(self, request):

        # 判断请求类型，根据请求类型做不同的请求
        if request.method.upper() == "GET":
            res = requests.get(url=request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == "POST":
            res = requests.post(url=request.url, headers=request.headers, params=request.params, data=request.data)
        else:
            raise Exception('该框架目前不支持{}类型的请求'.format(request.method))

        # 构建响应对象
        response = Response(url=res.url, headers=res.headers, code=res.status_code, body=res.content)

        # 将创建好的相应对象返回
        return response