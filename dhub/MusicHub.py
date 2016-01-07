from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BaseModel(Resource):
    def get(self):
        return {'url': 'http://mr7.doubanio.com/582708ab0bc27ab9394300ebb729750d/1/fm/song/p34721_128k.mp4'}

class MusicModel(BaseModel):
	def hello(sef):
		return ""

api.add_resource(MusicModel, '/music')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')