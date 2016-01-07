__author__ = 'starnet'

from model import BaseModel

class Music(BaseModel):
    url=''
	def __init__(self, url):
        self.url = url

    def get(self):
        return Music('http://www.baidu.com').tojson()
