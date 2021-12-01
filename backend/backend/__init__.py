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

@app.route('/')
def home():
    return "hello world"


from backend.routes import problem
api.add_resource(problem, "/problem")

from backend.routes import login
api.add_resource(login, "/login")

from backend.routes import signup
api.add_resource(signup, "/signup")

from backend.routes import user_profile
api.add_resource(user_profile, "/user/<int:user_id>/profile")

from backend.routes import submission
api.add_resource(submission, "/submission/new")

# from backend.routes import problem, problem_post_args
# api.add_resource(problem, "/problem/<int:problem_id>")