from flask import Flask, render_template, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config.from_object(Config)


if __name__=="__main__":
    app.run(debug=True)
