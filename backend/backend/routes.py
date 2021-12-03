from flask import jsonify
from flask_restful import Api, Resource
import datetime
from backend.exception import if_email_has_existed, if_username_has_existed, if_problemname_has_existed
from backend.models import Homework, Problem, User, Submission, User_problem, Queue
from backend import bcrypt
from backend.argument import signup_post_args, submission_post_args, login_post_args, user_profile_put_args, problem_post_args, problem_get_args, queue_post_args

import json

class problem(Resource):
    def get(self):
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
        return "problem is not found",404

    def post(self):
        problem = problem_post_args.parse_args()
        if_problemname_has_existed(problem.name)
        new_problem = Problem(questioner_id=problem.questioner_id,name=problem.name,difficulty=problem.difficulty,content=problem.content,time_limit=problem.time_limit,memory_limit=problem.memory_limit,testcase_count=problem.testcase_count,sample_input=problem.sample_input,is_hidden=problem.is_hidden,upload_date = datetime.datetime.now())
        from backend import db
        db.session.add(new_problem)
        db.session.commit()
        return "Success to add problem",200

# class problem(Resource):

class signup(Resource): 
    def post(self):
        args = signup_post_args.parse_args()
        if_username_has_existed(args.name)
        if_email_has_existed(args.email)
        if(args.password!=args.confirm_password):
            return "Confirm_password isn't equal to password!"
        hashed_password = bcrypt.generate_password_hash(args.password).decode('utf-8')
        new_user = User(name=args.name, email=args.email, password=hashed_password, register_date=datetime.datetime.now())
        #時間這邊，我先將這個{+datetime.timedelta(hours = 8)}拿掉，用臺灣當伺服器好像就是這邊的標準時間了
        from backend import db
        db.session.add(new_user)
        db.session.commit()
        return "Success to sign up", 200 

class login(Resource):
    def post(self):
        from backend import db
        args = login_post_args.parse_args()
        user = User.query.filter_by(email=args.email).first()
        if user and bcrypt.check_password_hash(user.password, args.password):
            return "success to login", 200
        elif user:
            return "Password is wrong"
        else:
            return "Couldn't find the user", 404

class user_profile(Resource):
    def get(self, user_id):
        from backend import db
        user = User.query.filter_by(user_id=user_id).first()
        if user: 
<<<<<<< HEAD
            return user.as_dict()
=======
            return user.__repr__()  
>>>>>>> 8ee181259e29a217937f244b97033bb94cb92e2b
        return 404
    def put(self):
        args = user_profile_put_args.parse_args()
        if_username_has_existed(args.name)
        if_email_has_existed(args.email)
        self = args
        from backend import db
        db.session.commit()

class submission_data(Resource):
    def get(self, submission_id):
        from backend import db
        submission = Submission.query.filter_by(submission_id=submission_id).first()
        if submission:
            return submission.__repr__()
        return 404
class submission_new(Resource):
    def post(self):
        from backend import db
        args = submission_post_args.parse_args()
        new_submission = Submission(user_id=args.user_id, problem_id=args.problem_id, source_id=args.source_id, status=args.status, error_hint=args.error_hint, error_line=args.error_line, language=args.language, time_used=args.time_used, memory_used=args.memory_used, exam_id=args.exam_id, homework_id=args.homework_id, upload_date=datetime.datetime.now(), code_content=args.code_content)
        db.session.add(new_submission)
        db.session.commit()
        return 200

class queue_data(Resource):
    def get(self):
        from backend import db
        queue = Queue.query.filter_by(mode=1).first()
        #jsonString = json.dumps(queue)
        if queue:   
            return queue.__repr__()
        return 404
class queue_new(Resource):
    def post(self):
        from backend import db
        args = queue_post_args.parse_args()
        new_queue = Queue(user_id=args.user_id, problem_id=args.problem_id, mode=args.mode, exam_id=args.exam_id, homework_id=args.homework_id, language=args.language, upload_date=str(datetime.datetime.now()), status=args.status, code_content=args.code_content)
        db.session.add(new_queue)
        db.session.commit()
        return 200