from flask_restful import Api, Resource, reqparse, abort
import datetime
# import json

problem_post_args = reqparse.RequestParser()
problem_post_args.add_argument("name",type=str,required=True,help='name is required!')
problem_post_args.add_argument("questioner_id",type=int,required=True,help='questioner_id is required!')
problem_post_args.add_argument("difficulty",type=int,required=True,help='difficulty is required!')
problem_post_args.add_argument("content",type=str,required=True,help='content is required!')
problem_post_args.add_argument("time_limit",type=int,required=True,help='time_limit is required!')
problem_post_args.add_argument("memory_limit",type=int,required=True,help='memory_limit is required!')
problem_post_args.add_argument("testcase_count",type=int,required=True,help='testcase_count is required!')
problem_post_args.add_argument("sample_input",type=str,required=True,help='sample_input is required!')
problem_post_args.add_argument("is_hidden",type=int,required=True,help='is_hidden is required!')

problem_get_args = reqparse.RequestParser()
# problem_get_args.add_argument("page",type=int,required=True,help='page is required!')
problem_get_args.add_argument("difficulty",type=int)
problem_get_args.add_argument("name",type=str)


class problem(Resource):
    def get(self):
        from backend.models import Problem
        problem=problem_get_args.parse_args()
        # print(problem["difficulty"],problem["name"])
        # searchfor = {}
        # if problem.difficulty:
        #     searchfor["difficulty"]=problem.difficulty
        # if problem.name:
        #     searchfor["name"]=problem.name
        # json_obj=json.dumps(dict(searchfor))
        # problem=Problem.query.filter_by()

        if problem:
            return problem
        return 404

    def post(self):
        from backend.models import Problem
        problem = problem_post_args.parse_args()
        # Problem.query.get(Problem.name)
        # if problem.
        new_problem = Problem(questioner_id=problem.questioner_id,name=problem.name,difficulty=problem.difficulty,content=problem.content,time_limit=problem.time_limit,memory_limit=problem.memory_limit,testcase_count=problem.testcase_count,sample_input=problem.sample_input,is_hidden=problem.is_hidden,upload_date = datetime.datetime.now()+datetime.timedelta(hours = 8))
        from backend import db
        db.session.add(new_problem)
        db.session.commit()
        return 200

signup_post_args = reqparse.RequestParser()
signup_post_args.add_argument("name", type=str, required=True, help='Username is necessary!')
signup_post_args.add_argument("email", type=str, required=True, help='Email is necessary!')
signup_post_args.add_argument("password", type=str, required=True, help='Password is necessary!')
signup_post_args.add_argument("confirm_password", type=str, required=True, help='Confirm_password is necessary!')

def if_username_has_existed(name):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(name).first()
    if user:
       abort(409, message="Existed Username")
def if_email_has_existed(email):
    from backend.models import User
    from backend import db
    user = User.query.filter_by(email).first()
    if user:
        abort(409, message="Existed Email")

class signup(Resource): 
    def post(self):
        from backend.models import User
        from backend import bcrypt
        args = signup_post_args.parse_args()
#       if_username_has_existed(args.name)
        if_email_has_existed(args.email)
        if(args.password!=args.confirm_password):
            return "Confirm_password isn't equal to password!"
        hashed_password = bcrypt.generate_password_hash(args.password).decode('utf-8')
        new_user = User(user_name=args.name, email=args.email, password=hashed_password, register_date=datetime.datetime.now()+datetime.timedelta(hours=8))
        from backend import db
        db.session.add(new_user)
        db.session.commit()
        return "Success to sign up", 200 

login_post_args = reqparse.RequestParser()
login_post_args.add_argument("email", type=str, required=True, help='Email is necessary!')
login_post_args.add_argument("password", type=str, required=True, help='Password is necessary!')

class login(Resource):
    def post(self):
        from backend.models import User
        from backend import db
        from backend import bcrypt
        args = login_post_args.parse_args()
        user = User.query.filter_by(args.email).first()
        if user and bcrypt.check_password_hash(user.password, args.password):
            return "success to login", 200
        elif user:
            return "Password is wrong"
        else:
            return "Couldn't find the user", 404

user_profile_get_args = reqparse.RequestParser()
user_profile_get_args.add_argument("name", type=str)
user_profile_get_args.add_argument("email", type=str)
user_profile_get_args.add_argument("user_to_problem", type=str)

user_profile_put_args = reqparse.RequestParser()
user_profile_put_args.add_argument("name", type=str)
user_profile_put_args.add_argument("email", type=str)
user_profile_put_args.add_argument("password", type=str)

class user_profile(Resource):
    def get(self):
        from backend.models import User, User_problem
        from backend import db
        args = user_profile_get_args.parse_args()
        user = User.query.filter_by(args.name).first()
        if user: 
            return user
        return 404
    def put(self):
        from backend.models import User
        args = user_profile_put_args.parse_args()
        if_username_has_existed(args.name)
        if_email_has_existed(args.email)
        self = args
        from backend import db
        db.session.commit()

