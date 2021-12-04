from flask import jsonify
from flask_restful import Api, Resource
import datetime
from backend.exception import if_email_has_existed, if_username_has_existed, if_problemname_has_existed, is_email_format, confirm_password_equal_password
from backend.models import Homework, Problem, User, Submission, User_problem, Queue, Problem_Testcase
from backend import bcrypt
from backend.argument import signup_post_args, submission_post_args, login_post_args, user_profile_put_args, problem_post_args, problem_get_args, queue_post_args, dispatcher_post_args

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
        new_problem = Problem(questioner_id=problem.questioner_id,name=problem.name,difficulty=problem.difficulty,content=problem.content,time_limit=problem.time_limit,memory_limit=problem.memory_limit,testcase_count=problem.testcase_count,sample_input=problem.sample_input,is_hidden=problem.is_hidden,upload_date = datetime.datetime.now(),correct_source_code = problem.correct_source_code)
        from backend import db
        db.session.add(new_problem)
        db.session.commit()
        return "Success to add problem",200

# class problem(Resource):

class signup(Resource): 
    def post(self):
        args = signup_post_args.parse_args()
        if_username_has_existed(args.name)
        is_email_format(args.email)
        if_email_has_existed(args.email)
        confirm_password_equal_password(args.password, args.confirm_password)
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
        user = User.query.filter_by(user_id=user_id).first_or_404()
        return user.as_dict()
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
        submission = Submission.query.filter_by(submission_id=submission_id).first_or_404()
        return submission.__repr__()

class queue_new(Resource):
    def post(self):
        from backend import db
        args = queue_post_args.parse_args()
        
        new_queue = Queue(user_id=args.user_id, problem_id=args.problem_id, mode=args.mode, exam_id=args.exam_id, homework_id=args.homework_id, language=args.language, upload_date=str(datetime.datetime.now()), code_content="123")
        db.session.add(new_queue)
        db.session.commit()
        return 200


class dispatcher(Resource):
    def get(self):
        from backend import db
        from backend.convert_file_to_json import convert_file_to_json as yea
        queues = Queue.query.limit(10).all()
        datas = {}
        s = "C:/Users/a2320/Desktop/coding/mochi/backend/backend/1.c"
        datas["Submission_Count"]=len(queues)
        datas["Submission_Set"]=[]
        cnt=0
        for queue in queues:
            data={}
            data["Mode"]=queue.mode
            data["Problem_id"]=queue.problem_id
            data["Source_id"]=queue.source_id
            problem=Problem.query.filter_by(problem_id=queue.problem_id).first()
            data["Test_case_count"]=problem.testcase_count
            data["Time_limit"]=problem.time_limit
            data["Memory_limit"]=problem.memory_limit
            data["Language"]=queue.language
            # data["Correct_source_code"]=problem.correct_source_code
            data["Code"]=yea(s)
            data["All_test_case_general_submission"]=[]
            testcases = Problem_Testcase.query.filter_by(problem_id=queue.problem_id).all()
            for i in range(10):
                data["All_test_case_general_submission"].append({"Test_case_name":i,"Test_case_answer_name":i})
            datas["Submission_Set"].append(data)
        
        return jsonify(datas)


    def post(self):
        from backend import db
        args = dispatcher_post_args.parse_args()
        print(args)
        count = args["Return_count"]
        for submission in args["Return_Set"]:
            data=Queue.query.filter_by(source_id=submission["Source_id"]).first()
            new_submission = Submission(user_id=data.user_id,problem_id=data.problem_id,source_id=submission["Source_id"],status=submission["Status"],code_content="123",exam_id=data.exam_id,homework_id=data.homework_id,error_hint=submission["Compile_error_out"],error_line=0,language=data.language,time_used=submission["Time"],memory_used=submission["Memory"],upload_date=data.upload_date)
            db.session.add(new_submission)
            # db.session.delete
            Queue.query.filter_by(source_id=submission["Source_id"]).delete()
            db.session.commit()
        return "success to return", 200

