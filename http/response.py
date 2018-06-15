class Response(object):

    def __init__(self,url,headers,code,body=None):
        # 请求方式header只获取响应头不需要响应内容,body为空,比如迅雷
        self.url = url
        self.headers =headers
        self.code = code
        self.body = body