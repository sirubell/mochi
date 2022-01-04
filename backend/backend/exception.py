from flask_restful import abort
from flask_login import current_user
import re

def if_problemname_has_existed(name,problem_id=-1):
    from backend.models import Problem
    from backend import db
    problem = Problem.query.filter_by(name=name).first()
    if problem and problem.problem_id != problem_id:
       abort(409, message="Existed Problemname")


def if_username_has_existed(name):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(name=name).first()
    if user == current_user:
        return
    elif user:
       abort(409, message="Existed Username")
       
def if_email_has_existed(email):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(email=email).first()
    if user == current_user:
        return
    elif user:
        abort(409, message="Existed Email")

def is_email_format(emailaddr):
    email_format = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if(not email_format.match(emailaddr)):
        abort(400, message="Request invalid: The format of email is invalid!")

def confirm_password_equal_password(password, confirm_password):
    if(password != confirm_password):
        abort (400, message="Confirm_password isn't equal to password!")


def reset_check_email(emailaddr):
    from backend.models import User
    email_format = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if(not email_format.match(emailaddr)):
        abort(400, message="Request invalid: The format of email is invalid!")        
    user = User.query.filter_by(email=emailaddr).first()
    if user is None:
        abort(404, message="There is no account with the email. You must register first.")

