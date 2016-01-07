__author__ = 'starnet'

from model import BaseModel

class Music(BaseModel):
    url='http://www.baidu.com'
    def __init__(self, url):
        self.url = url
