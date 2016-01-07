from flask import Flask
from flask_restful import Api
from models.model import Music

app = Flask(__name__)
api = Api(app)

api.add_resource(Music, '/music')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')