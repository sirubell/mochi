from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config.from_object(Config)

from backend.routes import problem, problem_post_args
api.add_resource(problem, "/problem")