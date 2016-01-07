__author__ = 'starnet'
from flask_restful import Resource


class BaseModel(Resource):
    def get(self):
        return {'url': 'http://mr7.doubanio.com/582708ab0bc27ab9394300ebb729750d/1/fm/song/p34721_128k.mp4'}