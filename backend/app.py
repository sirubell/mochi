from flask import Flask
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

if __name__=="__main__":
    app.run(debug=True)
