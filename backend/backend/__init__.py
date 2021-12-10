from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config
from flask_login import LoginManager


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config.from_object(Config)
login_manager = LoginManager(app)

@app.route('/')
def home():
    return "hello world"


from backend.routes import problem
api.add_resource(problem, "/problem")

from backend.routes import problem_id
api.add_resource(problem_id, "/problem/<int:problem_id>")

from backend.routes import problem_solution
api.add_resource(problem_solution,"/problem/<int:problem_id>/solution")

from backend.routes import problem_submission
api.add_resource(problem_submission, "/problem/<int:problem_id>/submission/<int:user_id>")

from backend.routes import status
api.add_resource(status, "/status/<int:page>")

from backend.routes import login
api.add_resource(login, "/login")

from backend.routes import logout
api.add_resource(logout, "/logout")

from backend.routes import signup
api.add_resource(signup, "/signup")

from backend.routes import user_profile
api.add_resource(user_profile, "/user/<int:user_id>/profile")

from backend.routes import submission_data
api.add_resource(submission_data, "/submission/<int:submission_id>")

from backend.routes import queue_new
api.add_resource(queue_new, "/submission/new")

from backend.routes import dispatcher
api.add_resource(dispatcher,"/dispatcher")


# from backend.routes import problem, problem_post_args
# api.add_resource(problem, "/problem/<int:problem_id>")