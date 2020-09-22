from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Pong(Resource):
    def get(self):
        return

api.add_resource(Pong, '/')
