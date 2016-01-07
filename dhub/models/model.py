__author__ = 'starnet'
from flask_restful import Resource
import json

class BaseModel(Resource):
    def get(self):
        return self.tojson()

    def tojson(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)