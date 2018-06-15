class Item(object):
    def __init__(self,data):
        self._data = data

    @property # 把方法变成可调用的属性形式
    def data(self):
    # 避免被修改,定义方法来获取属性
        return self._data
