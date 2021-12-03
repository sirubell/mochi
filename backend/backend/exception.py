from flask_restful import abort

def if_problemname_has_existed(name):
    from backend.models import Problem
    from backend import db
    problem = Problem.query.filter_by(name=name).first()
    if problem:
       abort(409, message="Existed Problemname")


def if_username_has_existed(name):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(name=name).first()
    if user:
       abort(409, message="Existed Username")
       
def if_email_has_existed(email):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(email=email).first()
    if user:
        abort(409, message="Existed Email")
