class Request(object):
    def __init__(self, url, method='GET', params=None, headers=None, data=None):
        self.url = url
        self.method = method
        self.params = params
        self.headers = headers
