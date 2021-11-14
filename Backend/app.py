from flask import Flask, render_template, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from config import Config
from api import problem, problem_post_args

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config.from_object(Config)

api.add_resource(problem, "/problem")

class problem(Resource):
    def get(self):
        return {"string":"Hello_world"}

    def post(self):
        problem = problem_post_args()
        new_problem = Problem(problem_name=problem.name,problem_content=problem.contemp,difficulty=problem.difficulty,questioner=problem.questioner_id,is_hidden=problem.is_hidden)
        return new_problem

if __name__=="__main__":
    app.run(debug=True)
