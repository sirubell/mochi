from flask_restful import Api, Resource
from app import api

class problem(Resource):
    def get(self):
        return {"string":"Hello_world"}

api.add_resource(problem, "/problem")