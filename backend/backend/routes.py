from flask import json, jsonify, url_for, redirect, flash, render_template, request
from flask_login.utils import login_required
from flask_restful import Api, Resource, abort
from flask_mail import Message
import datetime
from backend.exception import *
from backend.models import *
from backend import bcrypt, app, mail
from backend.config import parentdir
from backend.argument import *
import shutil
#from backend.argument import signup_post_args, submission_post_args, login_post_args, user_profile_put_args, problem_post_args, problem_put_args, problem_get_args, queue_post_args, dispatcher_post_args
# 8同理9
from flask_login import login_user, current_user, logout_user, login_required
import os

buffer_dir = os.path.join(parentdir, 'buffer')
problem_dir = os.path.join(parentdir, 'Problem')


class lazy(Resource):
    def get(self):
        from backend.convert_file_to_json import convert_file_to_testcase
        return convert_file_to_testcase()

    def post(self):
        if 'lan' in request.args:
            lan = request.args['lan']
        else:
            return "Error, lan is required"
        from backend.convert_file_to_json import convert_file_to_code
        return convert_file_to_code(lan)


class check(Resource):
    def get(self):
        queues = Queue.query.all()
        res = {}
        res["returnSet"] = []
        for q in queues:
            res["returnSet"].append(q.as_dict())
        return res


class delete_dir(Resource):
    def delete(self):
        shutil.rmtree(buffer_dir)
        os.mkdir(buffer_dir)

        problem_dir = os.path.join(parentdir, 'Problem')
        if os.path.isdir(problem_dir):
            shutil.rmtree(problem_dir)
            os.mkdir(problem_dir)
        return "delete success"


class reset_database(Resource):
    def delete(self):
        from backend import db
        db.drop_all()
        db.create_all()
        db.session.commit()
        return "delete success"


class problem(Resource):
    def get(self):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            return jsonify({'message': "Error, page is required", 'code': 500})
        XD = 1 # topic
        # topic = None
        difficulty = None
        name = None
        # if 'topic' in request.args:
        #     topic = request.args['topic']
        if 'difficulty' in request.args:
            difficulty = request.args['difficulty']
        if 'name' in request.args:
            name = request.args['name']
        if difficulty and name:
            problems = Problem.query.filter(db.and_(Problem.difficulty==difficulty,Problem.name.like(name))).paginate(per_page=20, page=page).order_by(Problem.problem_id)
        elif difficulty:
            problems = Problem.query.filtery_by(difficulty=difficulty).paginate(per_page=20, page=page).order_by(Problem.problem_id)
        elif name:
            problems = Problem.query.filter(Problem.name.like(name)).paginate(per_page=20, page=page).order_by(Problem.problem_id)
        else:
            problems = Problem.query.paginate(per_page=20, page=page).order_by(Problem.problem_id)

        if problems:
            ret = {}
            ret["status"]=200
            ret["returnset"] = []
            for problem in problems.items:
                ret["returnset"].append({
                    "id": problem.problem_id,
                    "name": problem.name,
                    "difficulty": problem.difficulty
                })
            return jsonify(ret)

    def post(self):
        problem = problem_post_args.parse_args()
        if_problemname_has_existed(problem.name)
        now = Queue.query.filter_by(source_id=problem.source_id).first()
        if now == None:
            return jsonify({'message': 'source_id is not found', 'code': 404})

        if now.status == None:
            return jsonify({'message': "pending", 'code': 500})

        if not os.path.isdir(buffer_dir):
            os.mkdir(buffer_dir)
        path = os.path.join(buffer_dir, str(now.user_id))
        with open(path+"/"+str(1)+'.in', mode="r", encoding="utf-8") as file:
            sample_input = file.read()
        with open(path+"/"+str(1)+'.ans', mode="r", encoding="utf-8") as file:
            sample_output = file.read()
        new_problem = Problem(questioner_id=problem.questioner_id, name=problem.name, difficulty=problem.difficulty, content=problem.content, time_limit=now.time_limit, memory_limit=now.memory_limit,
                              testcase_count=now.test_case_count, sample_input=sample_input, sample_output=sample_output, is_hidden=problem.is_hidden, upload_date=datetime.datetime.now(), correct_source_code=now.code_content, correct_answer_language=now.language)

        if not os.path.isdir(problem_dir):
            os.mkdir(problem_dir)
        # os.rename(buffer_dir+'/'+str(now.user_id)+'/'+str(now.source_id)+'.ansexe',
        #           buffer_dir+'/'+str(now.user_id)+'/'+str(Problem.query.count()+1)+'.ansexe')
        shutil.move(path, os.path.join(
            problem_dir, str(Problem.query.count()+1)))
        from backend import db
        for i in range(now.test_case_count):
            test_case = Problem_Testcase(problem_id=Problem.query.count(
            )+1, testcase_id=i+1, input_name=str(i+1)+'.in', output_name=str(i+1)+'.ans')
            db.session.add(test_case)
        db.session.add(new_problem)
        db.session.delete(now)
        db.session.commit()
        users = User.query.all()
        for user in users:
            new_user_problem = User_problem(
                user_id=user.id, problem_id=new_problem.problem_id, status=0)
            db.session.add(new_user_problem)
        db.session.commit()
        return jsonify({'message': "Success to add problem", 'code': 200})


class create_problem_test_run(Resource):
    def get(self):
        if 'source_id' in request.args:
            source_id = int(request.args['source_id'])
        else:
            return jsonify({'message': "Error, source_id is required", 'code': 500})

        if 'user_id' in request.args:
            user_id = int(request.args['user_id'])
        else:
            return jsonify({'message': "Error, user_id is required", 'code': 500})
        now = Queue.query.filter_by(source_id=source_id).first()
        if now == None:
            return jsonify({'message': 'source_id is not found', 'code': 404})
        if now.status == None:
            return jsonify({'message': "pending", 'code': 500})
        if now.status == "AC":
            if not os.path.isdir(buffer_dir):
                os.mkdir(buffer_dir)
            path = os.path.join(buffer_dir, str(user_id))
            res = {}
            res["status"] = "AC"
            res["test_case_count"] = now.test_case_count
            res["return_set"] = []
            for i in range(now.test_case_count):
                with open(path+"/"+str(i+1)+'.ans', mode="r", encoding="utf-8") as file:
                    temp = file.read()
                    res["return_set"].append(temp)
            return jsonify(res)
        else:
            if not os.path.isdir(buffer_dir):
                os.mkdir(buffer_dir)
            path = os.path.join(buffer_dir, str(user_id))
            shutil.rmtree(path)
            status = now.status
            error_message = now.error_message
            db.session.delete(now)
            db.session.commit()
            return jsonify({'status': status, 'message': error_message})

    def post(self):
        args = create_problem_test_run_args.parse_args()
        if args.time_limit > 5 or args.time_limit < 0:
            return jsonify({"message": "invalid_time_limit", 'code': 500})
        if args.memory_limit > 5120 or args.memory_limit < 6:
            return jsonify({"message": "invalid_memory_limit", 'code': 500})
        if not os.path.isdir(buffer_dir):
            os.mkdir(buffer_dir)
        path = os.path.join(buffer_dir, str(args.user_id))
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            from backend import db
            shutil.rmtree(path)
            os.mkdir(path)
            last_q = Queue.query.filter_by(
                user_id=args.user_id, mode=3).first()
            if last_q != None:
                db.session.delete(last_q)
                db.session.commit()
        input_set = args["test_case"]
        if len(input_set) == 0:
            return jsonify({'message': "test_case can't be empty!", 'code': 500})
        new_queue = Queue(user_id=args.user_id, mode=3, language=args.language, test_case_count=len(
            input_set), upload_date=datetime.datetime.now(), code_content=args.code_content, time_limit=args.time_limit, memory_limit=args.memory_limit)
        from backend import db
        db.session.add(new_queue)
        db.session.commit()

        # omgomg
        with open(path+"/"+"correct_source_code"+'.'+str(args.language), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)
        cnt = 1
        for testcase in input_set:
            with open(path+'/'+str(cnt)+".in", mode='w', encoding="utf-8") as file:
                file.write(testcase)
            cnt += 1

        return jsonify({'code': 200, 'source_id': new_queue.source_id})


class test_run(Resource):
    def get(self):
        if 'source_id' in request.args:
            source_id = int(request.args['source_id'])
        else:
            return jsonify({'message': "Error, source_id is required", 'code': 500})
        if 'user_id' in request.args:
            user_id = int(request.args['user_id'])
        else:
            return jsonify({'message': "Error, user_id is required", 'code': 500})
        now = Queue.query.filter_by(source_id=source_id).first()
        if now.status == None:
            return jsonify({'message': "pending", 'code': 500})
        
        # from backend.convert_file_to_json import convert_file_to_json as yea
        # res = yea("buffer/"+str(source_id)+'.ans')
        from backend import db
        if now.status in ['AC','WA']:
            if not os.path.isdir(buffer_dir):
                os.mkdir(buffer_dir)
            with open(os.path.join(buffer_dir, str(source_id)+".ans"), mode="r", encoding="utf-8") as file:
                res = file.read()
            with open(os.path.join(buffer_dir, str(source_id)+".cans"), mode="r", encoding="utf-8") as file:
                res2 = file.read()
            db.session.delete(now)
            db.session.commit()
            return jsonify({'message':'OK','output':res,'status':now.status,'correct_ans_output':res2})
        db.session.delete(now)
        db.session.commit()
        return jsonify({'message':now.error_message,'output':"",'status':now.status})

    def post(self):
        from backend import db
        args = test_run_post_args.parse_args()
        if not os.path.isdir(buffer_dir):
            os.mkdir(buffer_dir)
        new_queue = Queue(user_id=args.user_id, mode=2, problem_id=args.problem_id, language=args.language,
                          upload_date=datetime.datetime.now(), code_content=args.code_content, test_case_count=1)
        source_id = Queue.query.count()+1
        with open(os.path.join(buffer_dir, str(source_id) + ".in"), mode="w", encoding="utf-8") as file:
            file.write(args.test_case)
        with open(os.path.join(buffer_dir, str(source_id) + '.' + str(args.language)), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)
        db.session.add(new_queue)
        db.session.commit()
        return jsonify({'code': 200, 'source_id': source_id})


class problem_id(Resource):
    def get(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id).first()
        if problem == None:
            return jsonify({'code':404,'message':'problem is not found'})
        return problem.as_dict()

    #!!
    def put(self, problem_id):
        args = problem_put_args.parse_args()
        problem = Problem.query.filter_by(problem_id=problem_id).first()
        XD = 1
        # problem_testcase = Problem_Testcase.query.filter_by(problem_id=problem_id).all()
        if args.source_id !=-1:
            XD = 1
        if problem == None:
            return jsonify({'message': "problem_id does not exist", 'code': 500})
        if args.name:
            if_problemname_has_existed(args.name, problem_id)
            problem.name = args.name
        if args.difficulty:
            problem.difficulty = args.difficulty
        if args.content:
            problem.content = args.content
        if args.time_limit:
            problem.time_limit = args.time_limit
        if args.memory_limit:
            problem.memory_limit = args.memory_limit
        if args.is_hidden:
            problem.is_hidden = args.is_hidden
        if args.correct_source_code:
            problem.correct_source_code = args.correct_source_code

        from backend import db
        db.session.commit()
        return jsonify({'message': "Success to put problem", 'code': 200})

    def delete(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id).first()
        if problem == None:
            return jsonify({'message':'problem is not found','code':404})
        if 'user_id' in request.args:
            user_id = int(request.args['user_id'])
        else:
            return jsonify({'message':'user_id is required','code':500})
        if problem.questioner_id != user_id:
            return jsonify({'message':'wrong user','code':403})
        problem_testcases = Problem_Testcase.query.filter_by(problem_id=problem_id).all()
        shutil.rmtree(problem_dir+'/'+str(problem_id))
        from backend import db
        for problem_testcase in problem_testcases:
            db.session.delete(problem_testcase)
        db.session.delete(problem)
        db.session.commit()
        return jsonify({'message': "Success to delete problem", 'code': 200})

class problem_solution(Resource):
    def get(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id)
        if problem == None:
            return jsonify({'message': "problem does not exist", 'code': 404})

        return jsonify({'solution': problem.correct_source_code,'code':200})


class status(Resource):
    def get(self):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            return jsonify({"message ": " Error, page is required",'code':500})
        user_id = None
        problem_id = None
        if 'user_id' in request.args:
            user_id = int(request.args['user_id'])
            user = User.query.filter_by(user_id=user_id).first()
            if user == None:
                return jsonify({'message':'user is not found','code':404})
        if 'problem_id' in request.args:
            problem_id = int(request.args['problem_id'])
            problem = Problem.query.filter_by(problem_id=problem_id).first()
            if problem == None:
                return jsonify({'message':'problem is not found','code':404})
        
        if user_id and problem_id:
            submissions = Submission.query.filter_by(user_id=user_id, problem_id=problem_id).order_by(Submission.submission_id.desc()).paginate(
                per_page=20, page=page)
        elif problem_id:
            submissions = Submission.query.filter_by(problem_id=problem_id).order_by(Submission.submission_id.desc()).paginate(
                per_page=20, page=page)
        elif user_id:
            submissions = Submission.query.filter_by(user_id=user_id).order_by(Submission.submission_id.desc()).paginate(
                per_page=20, page=page)
        else:
            submissions = Submission.query.order_by(Submission.submission_id.desc()).paginate(
                per_page=20, page=page)

        ret = {}
        ret['code'] = 200
        ret["returnset"] = []
        for submission in submissions.items:
            time = submission.upload_date
            user = User.query.filter_by(id=submission.user_id).first()
            ret["returnset"].append({
                "submission_id": submission.submission_id,
                "problem_id": submission.problem_id,
                "name": user.name,
                "status": submission.status,
                "language": submission.language,
                "upload_date": time.strftime("%Y/%m/%d %H:%M:%S")
            })
        return jsonify(ret)


class signup(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify({"message ": " Had logged in"})
        args = signup_post_args.parse_args()
        if_username_has_existed(args.name)
        is_email_format(args.email)
        if_email_has_existed(args.email)
        confirm_password_equal_password(args.password, args.confirm_password)
        hashed_password = bcrypt.generate_password_hash(
            args.password).decode('utf-8')
        new_user = User(name=args.name, email=args.email,
                        password=hashed_password, register_date=datetime.datetime.now())
        from backend import db
        db.session.add(new_user)
        db.session.commit()
        problems = Problem.query.all()
        for problem in problems:
            new_user_problem = User_problem(
                user_id=new_user.id, problem_id=problem.problem_id, status=0)
            db.session.add(new_user_problem)
        db.session.commit()
        return jsonify({"message ": " success to sigup"})


class login(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify({"message ": " Had login", "userId": current_user.id})
        args = login_post_args.parse_args()
        user = User.query.filter_by(email=args.email).first()
        if user and bcrypt.check_password_hash(user.password, args.password):
            login_user(user, remember=args.remember)
            return jsonify({"message ": " Success to login.", "userId": user.id})
        elif user:
            abort(400, message=" wrong password")
        else:
            abort(404, message="Couldn't find the user(no this email)")


class reset_sent_email(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify({"message ": " Had login", "userId": current_user.id})
        args = request_reset_post_args.parse_args()
        reset_check_email(args.email)
        user = User.query.filter_by(email=args.email).first()
        token = user.get_reset_token()
        recipient = args.email
        title = "Reset your password."
        msg = Message(title, recipients=[recipient])
        msg.body = "This is a email to change your password in mochi, please paste token to the validated page.\n Token is the following: "+token
        mail.send(msg)
        return jsonify({"message": "success to send a mail"})


class confirm_token(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify({"message ": " Had login", "userId": current_user.id})
        args = confirm_token_post_args.parse_args()
        user = User.verify_reset_token(args.token)
        if user is None:
            abort(404)


class reset_password(Resource):
    def put(self, token):
        if current_user.is_authenticated:
            return jsonify({"message ": " Had login", "userId": current_user.id})
        args = reset_password_put_args.parse_args()
        user = User.verify_reset_token(token)
        confirm_password_equal_password(args.password, args.confirm_password)
        hashed_password = bcrypt.generate_password_hash(
            args.password).decode('utf-8')
        user.password = hashed_password
        from backend import db
        db.session.commit()


class logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return jsonify({"message": "success to logout"})


class user_profile(Resource):
    @login_required
    def get(self, user_id):
        from backend import db
        user = User.query.filter_by(id=user_id).first_or_404()
        ACs = User_problem.query.filter_by(user_id=user.id, status=1).all()
        datas = []
        for AC in ACs:
            datas.append(AC.problem_id)
        return jsonify({"name": user.name, "email": user.email, "user_id": user.id, "register_date": str(user.register_date), "user_problem": datas})

    
class user_myprofile(Resource):
    @login_required
    def get(self):
        from backend import db
        user = current_user
        ACs = User_problem.query.filter_by(user_id=user.id, status=1).all()
        datas = []
        for AC in ACs:
            datas.append(AC.problem_id)
        return jsonify({"name": user.name, "email": user.email, "user_id": user.id, "register_date": str(user.register_date), "user_problem": datas})

class change_profile_name_email(Resource):
    @login_required
    def get(self):
        user = current_user
        return jsonify({"name": user.name, "email": user.email})
    def put(self):
        args = change_profile_name_email_put_args.parse_args()
        if_username_has_existed(args.name)
        is_email_format(args.email)
        if_email_has_existed(args.email)
        current_user.name = args.name
        current_user.email = args.email
        from backend import db
        db.session.commit()

class change_profile_password(Resource):
    @login_required
    def put(self):
        args = change_profile_password_put_args.parse_args()
        confirm_password_equal_password(args.password, args.confirm_password)
        hashed_password = bcrypt.generate_password_hash(
            args.password).decode('utf-8')
        current_user.password = hashed_password
        from backend import db
        db.session.commit()        

class submission_data(Resource):
    def get(self, submission_id):
        from backend import db
        submission = Submission.query.filter_by(
            submission_id=submission_id).first()
        if submission == None:
            return jsonify({'message': 'submission is not found', 'status': 404})
        return submission.as_dict()


class queue_new(Resource):
    def get(self):
        if 'source_id' in request.args:
            source_id = int(request.args['source_id'])
        else:
            return jsonify({'message': "Error, source_id is required", 'code': 404})
        now = Queue.query.filter_by(source_id=source_id).first()
        if now:
            return jsonify({'message':'not ok','code':500})
        submission = Submission.query.filter_by(source_id=source_id).first()
        if submission == None:
            return jsonify({'message':'unexpected error','code':404})
        return jsonify({'message':'ok','submission_id':submission.id,'code':200})


    def post(self):
        from backend import db
        args = queue_post_args.parse_args()
        problem = Problem.query.filter_by(problem_id=args.problem_id).first()
        if problem == None:
            return jsonify({'message':'problem is not found','code':404})
        upload_date = datetime.datetime.now()
        new_queue = Queue(user_id=args.user_id, problem_id=args.problem_id, mode=1, exam_id=args.exam_id,
                          homework_id=args.homework_id, language=args.language, upload_date=upload_date, code_content=args.code_content, test_case_count=problem.testcase_count)
        ret = {}
        if args.homework_id:
            homework =  Homework.query.filter_by(homework_id=args.homework_id).first()
            if homework == None:
                ret['code'] = 404
                ret['warning'] = 'homework is not found'
                return jsonify(ret)
        elif args.exam_id:
            exam = Exam.query.filter_by(exam_id=args.exam_id).first()
            if exam == None:
                ret['code'] = 404
                ret['warning'] = 'exam is not found'
                return jsonify(ret)
        db.session.add(new_queue)
        db.session.commit()
        if not os.path.isdir(buffer_dir):
            os.mkdir(buffer_dir)

        with open(os.path.join(buffer_dir, str(Queue.query.count()) + '.' + str(args.language)), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)

        ret['message'] = 'add queue success'
        ret['code'] = 200
        ret['warning'] = None
        if args.homework_id:
            homework =  Homework.query.filter_by(homework_id=args.homework_id).first()
            if upload_date > homework.deadline:
                ret['code'] = 500
                ret['warning'] = 'homework deadline is over'
                return jsonify(ret)

        elif args.exam_id:
            exam = Exam.query.filter_by(exam_id=args.exam_id).first()
            if upload_date > exam.end_time:
                ret['code'] = 500
                ret['warning'] = 'exam is end'
                return jsonify(ret)

        return jsonify({'message': 'success', 'code': 200, 'source_id':new_queue.source_id})


class dispatcher(Resource):
    def get(self):
        from backend import db
        from backend.convert_file_to_json import convert_file_to_json as yea
        queues = Queue.query.limit(10).all()
        datas = {}
        datas["Submission_Set"] = []
        cnt = 0
        for queue in queues:
            if queue.status != None:
                continue
            if cnt > 10:
                break
            data = {}
            data["Mode"] = queue.mode
            if queue.mode in [1, 2]:
                data["Problem_id"] = queue.problem_id
            data["User_id"] = queue.user_id
            data["Source_id"] = queue.source_id
            data["Keep"] = 0
            problem = Problem.query.filter_by(
                problem_id=queue.problem_id).first()
            if problem == None and queue.mode in [1, 2]:
                return jsonify({'message': 'problem is not found', 'code': 404})
            data["Test_case_count"] = queue.test_case_count
            if queue.mode in [1, 2]:
                data["Time_limit"] = problem.time_limit
                data["Memory_limit"] = problem.memory_limit
            else:
                data["Time_limit"] = queue.time_limit
                data["Memory_limit"] = queue.memory_limit
            data["Language"] = queue.language
            if queue.mode in [1, 2]:
                data["Correct_answer_language"] = problem.correct_answer_language
            if queue.mode in [1, 2]:
                data["Correct_source_code"] = problem.correct_source_code
            if queue.mode in [1, 2]:
                data["Code"] = yea(
                    "buffer/"+str(queue.source_id)+'.'+str(queue.language))
            else:
                data["Code"] = yea(
                    "buffer/"+str(queue.user_id)+"/correct_source_code"+'.'+str(queue.language))
            data["All_test_case_general_submission"] = []
            data["Self_test_case"] = []
            if queue.mode == 1:
                testcases = Problem_Testcase.query.filter_by(
                    problem_id=queue.problem_id).all()
                for i in range(len(testcases)):
                    data["All_test_case_general_submission"].append(
                        {"Test_case_name": testcases[i].input_name.replace('.in', ""), "Test_case_answer_name": testcases[i].output_name.replace('.ans', "")})

            if queue.mode == 2:
                data["Self_test_case"].append(
                    {"Test_case_name": str(queue.source_id),
                     "Data": yea(
                        "buffer/"+str(queue.source_id)+'.in')
                     })
            if queue.mode == 3:
                for i in range(queue.test_case_count):
                    data["Self_test_case"].append(
                        {"Test_case_name": str(i+1),
                         "Data": yea(
                            "buffer/"+str(queue.user_id)+"/"+str(i+1)+'.in')
                         })

            datas["Submission_Set"].append(data)
            cnt += 1

        datas["Submission_Count"] = cnt
        return jsonify(datas)

    def post(self):
        from backend import db
        args = dispatcher_post_args.parse_args()
        for submission in args["Return_Set"]:
            data = Queue.query.filter_by(
                source_id=submission["Source_id"]).first()
            if data == None:
                queues = Queue.query.all()
                res = {}
                res["returnSet"] = []
                res["disappeared_source_id"] = submission["Source_id"]
                for q in queues:
                    res["returnSet"].append(q.as_dict())
                print(res)
                continue
            if data.mode == 1:
                status = submission["Status"]
                if data.exam_id:
                    exam = Exam.query.filter_by(exam_id=data.exam_id).first()
                    dashboard = Dashboard.query.filter_by(
                        exam_id=data.exam_id, user_id=data.user_id).first()
                    dash = Dashboard_with_problem.query.filter_by(
                        exam_id=data.exam_id, user_id=data.user_id, problem_id=data.problem_id).first()
                    upload_date = data.upload_date
                    start_time = exam.start_time
                    end_time = exam.end_time
                    if end_time > upload_date:
                        timedelta = upload_date-start_time
                        solved_time = timedelta.total_seconds()//60
                        from backend import db
                        if dashboard == None:
                            dashboard = Dashboard(
                                exam_id=data.exam_id, user_id=data.user_id, solved_count=0, total_time=0)
                            db.session.add(dashboard)
                            db.session.commit()
                        if dash == None:
                            problem = Exam_problem.query.filter_by(
                                exam_id=data.exam_id, problem_id=problem_id).first()
                            if status != "AC":
                                dash = Dashboard_with_problem(
                                    exam_id=data.exam_id, user_id=data.user_id, problem_id=data.problem_id, sequence=problem.sequence, try_count=1, current_status=0)
                            else:
                                dash = Dashboard_with_problem(exam_id=data.exam_id, user_id=data.user_id, problem_id=data.problem_id,
                                                            sequence=problem.sequence, try_count=1, solved_time=solved_time, current_status=1)
                                dashboard.solved_count += 1
                                dashboard.total_time += dash.solved_time
                            db.session.add(dash)
                            db.session.commit()
                        else:
                            if dash.current_status != 1:
                                dash.try_count += 1
                            if status == 'AC':
                                if dash.current_status == 0:
                                    dash.current_status = 1
                                    dash.solved_time = solved_time
                                    dashboard.solved_count += 1
                                    dashboard.total_time += dash.solved_time + (dash.try_count - 1) * 20
                            db.session.commit()

                elif data.homework_id:
                    homework = Homework.query.filter_by(
                        homework_id=data.homework_id).first()
                    student = Class_user.query.filter_by(
                        class_id=homework.class_id, user_id=data.user_id).first()
                    homework_problem = Homework_problem.query.filter_by(
                        homework_id=data.homework_id).all()
                    homework_problem_status = Homework_problem_status.query.filter_by(
                        homework_id=data.homework_id, problem_id=data.problem_id, user_id=data.user_id).first()
                    upload_date = data.upload_date
                    deadline = homework.deadline
                    if upload_date < deadline:
                        if homework == None:
                            return jsonify({'message': "homework is not found", 'code': 404})
                        if homework_problem == None:
                            return jsonify({'message': "homework don't have this problem", 'code': 404})
                        if student == None:
                            return jsonify({'message': "user is not in the class", 'code': 404})
                        if homework_problem_status == None:
                            if status != "AC":
                                new_homework_problem_status = Homework_problem_status(
                                    homework_id=data.homework_id, problem_id=data.problem_id, user_id=data.user_id, hand_in_status=1)
                            else:
                                new_homework_problem_status = Homework_problem_status(
                                    homework_id=data.homework_id, problem_id=data.problem_id, user_id=data.user_id, hand_in_status=2)
                            db.session.add(new_homework_problem_status)
                            db.session.commit()
                        else:
                            if status != "AC" and homework_problem_status.hand_in_status == 0:
                                homework_problem_status.hand_in_status = 1
                            else:
                                homework_problem_status.hand_in_status = 2
                            db.session.commit()

                new_submission = Submission(user_id=data.user_id, problem_id=data.problem_id, source_id=submission["Source_id"], status=submission["Status"], code_content=data.code_content, exam_id=data.exam_id, homework_id=data.homework_id, error_hint=submission[
                    "Compile_error_out"], error_line=0, language=data.language, time_used=submission["Time"], memory_used=submission["Memory"], upload_date=data.upload_date)

                db.session.add(new_submission)
                db.session.delete(data)
                db.session.commit()

                XD = 1  # status 的定義
                user_problem = User_problem.query.filter_by(
                    user_id=data.user_id, problem_id=data.problem_id).first()
                if status == "AC":
                    user_problem.status = 1
                else:
                    user_problem.status = 0

            elif data.mode == 2:
                XD = 1  # compile_error_out 的 status
                data.status = submission["Status"]
                if data.status in ["AC","WA"]:
                    if not os.path.isdir(buffer_dir):
                        os.mkdir(buffer_dir)
                    with open(os.path.join(buffer_dir, str(data.source_id) + ".ans"), mode="w", encoding="utf-8") as file:
                        file.write(submission["All_stander_out"]
                                   [str(data.source_id)])
                    with open(os.path.join(buffer_dir, str(data.source_id) + ".cans"), mode="w", encoding="utf-8") as file:
                        file.write(submission["Correct_answer_out"])
                else:
                    data.error_message = submission["Compile_error_out"]

            else:
                XD = 1  # compile_error_out 的 status
                data.status = submission["Status"]
                if data.status == "AC":
                    if not os.path.isdir(os.path.join(buffer_dir, str(data.user_id))):
                        os.mkdir(os.path.join(buffer_dir, str(data.user_id)))
                    cnt = 1
                    for i in range(len(submission["All_stander_out"])):
                        with open(os.path.join(os.path.join(buffer_dir, str(data.user_id)), str(cnt)+".ans"), mode="w", encoding="utf-8") as file:
                            file.write(submission["All_stander_out"][str(i+1)])
                        cnt += 1
                else:
                    data.error_message = submission["Compile_error_out"]
        db.session.commit()
        return jsonify({'message': "success to return", 'code': 200})


class class_all(Resource):
    def get(self):  # 給所有班級資訊
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            return jsonify({'message': "Error, page is required", 'code': 404})

        classes = Class.query.all()
        ret = {}
        ret["returnset"] = []
        for a_class in classes:
            user = User.query.filter_by(id=a_class.teacher_id).first()
            ret["returnset"].append({
                "id": a_class.id,
                "name": a_class.name,
                "semester": a_class.semester,
                "teacher_name": user.name,
                "public": a_class.is_public
            })
        return jsonify(ret)

    def post(self):  # 新增班級，需要teacher的user_id,class_name,semester,is_public
        args = class_post_args.parse_args()
        teacher_id = args.user_id

        import random
        import string
        while 1:
            s = ''.join(random.choice(string.ascii_letters + string.digits)
                        for x in range(10))
            search = Class.query.filter_by(invite_code=s).first()
            if search == None:
                break

        user = User.query.filter_by(id=teacher_id).first()
        if user == None:
            return jsonify({'message': 'user is not exist', 'code': 404})
        new_class = Class(class_name=args.class_name, semester=args.semester, teacher_name=user.name,
                          is_public=args.is_public, invite_code=s, teacher_id=teacher_id)
        new_user_class = Class_user(class_id=Class.query.count(
        )+1, user_id=teacher_id, student_id=-1, authority=1)
        from backend import db
        db.session.add(new_class)
        db.session.add(new_user_class)
        db.session.commit()
        return jsonify({'message': "create success", 'invite code': s, 'code': 200})


class A_class(Resource):
    def get(self, class_id):
        a_class = Class.query.filter_by(class_id=class_id).first()
        if a_class == None:
            return jsonify({'message': "class is not found", 'code': 404})
        user = User.query.filter_by(id=a_class.teacher_id).first()
        ret = {
            "id": a_class.id,
            "name": a_class.name,
            "semester": a_class.semester,
            "teacher_name": user.name,
            "is_public": a_class.public,
            "invite_code": a_class.invite_code
        }
        return jsonify(ret)

    def put(self):  # 更新教室相關資訊
        args = class_put_args.parse_args()
        a_class = Class.query.filter_by(class_id=args.class_id).first()
        if a_class == None:
            return jsonify({'message': "class is not found", 'code': 404})
        if args.name:
            a_class.name = args.name
        if args.semester:
            a_class.semester = args.semester
        if args.teacher_name:
            a_class.teacher_name = args.teacher_name
        if args.is_public:
            a_class.is_public = args.is_public
        if args.invite_code:
            a_class.invite_code = args.invite_code
        return jsonify({'message': "create success", 'code': 200})


class class_member(Resource):
    def get(self, class_id):  # get教室成員
        a_class = Class_user.query.filter_by(class_id=class_id).all()
        if a_class == None:
            return jsonify({'message': "class is not found", 'code': 404})

        ret = {}
        ret["returnset"] = []
        for student in a_class:
            user = User.query.filter_by(id=student.user_id).first()
            ret["returnset"].append({
                "id": user.id,
                "name": user.name
            })
        return jsonify(ret)

    def post(self, class_id):  # 新增同學到教室，給我user_id和student_id(學號)更新table
        args = class_member_post_args.parse_args()
        user = User.query.filter_by(id=args.user_id).first()
        if user == None:
            return jsonify({'message': 'the user is not found', 'code': 404})
        the_class = Class.query.filter_by(class_id=class_id).first()
        if the_class == None:
            return jsonify({'message': "class is not found", 'code': 404})
        if the_class.invite_code != args.invite_code:
            return jsonify({'message': "invite code is wrong"})
        check = Class_user.query.filter_by(
            class_id=class_id, user_id=args.user_id, student_id=args.student_id).first()
        if check:
            return jsonify({'message': 'the student is already in the class'})
        new_user_class = Class_user(
            class_id=class_id, user_id=args.user_id, student_id=args.student_id, authority=0)
        from backend import db
        db.session.add(new_user_class)
        db.session.commit()
        return jsonify({'message': 'add member success', 'code': 200})

    def put(self, class_id):
        args = class_put_args.parse_args()
        a_class = Class(class_id=class_id).first()
        if args.user_id != a_class.teacher_id:
            return jsonify({'message': 'only teacher can refresh class infomation'})


class exam(Resource):
    def get(self, exam_id):
        exam = Exam.query.filter_by(exam_id=exam_id).first()
        if exam == None:
            return jsonify({'message': "exam is not found", 'code': 404})
        exam_problem = Exam_problem.query.filter_by(
            exam_id=exam_id).order_by(Exam_problem.sequence).all()
        ret = {}
        ret["class_id"] = exam.class_id
        ret["name"] = exam.name
        ret["start_time"] = exam.start_time.strftime("%Y/%m/%d %H:%M:%S")
        ret["end_time"] = exam.end_time.strftime("%Y/%m/%d %H:%M:%S")
        ret["exam_info"] = exam.exam_info
        ret["problem_set"] = []
        for a_problem in exam_problem:
            problem = Problem.query.filter_by(
                problem_id=a_problem.problem_id).first()
            ret["problem_set"].append({'exam_id':exam_id,'sequence':a_problem.sequence,'problem_name':problem.name,'problem_id':problem.problem_id})
        return jsonify(ret)


class add_exam(Resource):
    def post(self):  # 新增考試
        args = exam_post_args.parse_args()

        a_class = Class.query.filter_by(class_id=args.class_id).first()
        if a_class == None:
            return jsonify({'message': "class is not found", 'code': 404})
        if a_class.teacher_id != args.user_id:
            return jsonify({'message': "only teacher can create exam", 'code': 403})

        for a_problem in args.problem_set:
            problem = Problem.query.filter_by(problem_id=a_problem).first()
            if problem == None:
                return jsonify({'message': "problem id = " + str(a_problem) + " is not found", 'code': 404})
        start_time = datetime.datetime.strptime(args.exam_start_time, "%Y/%m/%d %H:%M:%S")
        end_time = datetime.datetime.strptime(args.exam_end_time, "%Y/%m/%d %H:%M:%S")
        exam = Exam(class_id=args.class_id, name=args.exam_name, start_time=start_time,
                    end_time=end_time, exam_info=args.exam_info)
        from backend import db
        db.session.add(exam)
        db.session.commit()
        cnt = 1
        for a_problem in args.problem_set:
            new_exam_problem = Exam_problem(
                exam_id=Exam.query.count(), problem_id=a_problem, sequence=cnt)
            cnt += 1
            db.session.add(new_exam_problem)

        db.session.commit()
        problem_set = Exam_problem.query.filter_by(exam_id=Exam.query.count()).all()
        students = Class_user.query.filter_by(class_id=args.class_id).all()
        from backend import db
        for student in students:
            new_dashboard = Dashboard(exam_id=Exam.query.count(), user_id=student.user_id)
            db.session.add(new_dashboard)
            for problem in problem_set:
                dash = Dashboard_with_problem(exam_id=Exam.query.count(), user_id=student.user_id, problem_id=problem.problem_id,
                                              sequence=problem.sequence)
                db.session.add(dash)
        db.session.add(exam)
        db.session.commit()
        return jsonify({'message': "success to add exam", 'code': 300})


class dashboard(Resource):
    def get(self, exam_id):  # 回傳dashboard table
        lines = Dashboard.query.filter_by(exam_id=exam_id).order_by(Dashboard.solved_count.desc()).order_by(Dashboard.total_time).all()
        if lines == None:
            return jsonify({'message': "Error, dashboard hadn't been created", 'code': 404})
        problem_set = []
        exam_problems = Exam_problem.query.filter_by(exam_id=exam_id).all()
        for exam_problem in exam_problems:
            problem_set.append(exam_problem.problem_id)
        ret = {}
        ret["return_set"] = []
        for line in lines:
            user = User.query.filter_by(id=line.user_id).first()
            a_student = {}
            a_student["name"] = user.name
            a_student["solved"] = line.solved_count
            a_student["total_time"] = line.total_time
            dashs = Dashboard_with_problem.query.filter_by(
                exam_id=exam_id,user_id=line.user_id).all()
            a_student["problem"] = []
            for dash in dashs:
                problem = {}
                problem["sequence"]=dash.sequence
                problem["status"]=dash.current_status
                problem["solved_time"]=dash.solved_time
                problem["try_count"]=dash.try_count
                a_student["problem"].append(problem)
            ret["return_set"].append(a_student)
        return jsonify(ret)
        


class add_homework(Resource):
    def post(self):
        args = homework_post_args.parse_args()
        problem_set = args.problem_set

        a_class = Class.query.filter_by(class_id=args.class_id).first()

        if a_class == None:
            return jsonify({'message': "class is not found", 'code': 404})

        if args.user_id != a_class.teacher_id:
            return jsonify({'message': "only teacher can create homework", 'code': 500})

        for a_problem in problem_set:
            problem = Problem.query.filter_by(problem_id=a_problem).first()
            if problem == None:
                return jsonify({'message': "problem id = " + str(a_problem) + " is not found", 'code': 404})

        upload_time = datetime.datetime.strptime(args.upload_time, "%Y/%m/%d %H:%M:%S")
        deadline = datetime.datetime.strptime(args.deadline, "%Y/%m/%d %H:%M:%S")
        homework = Homework(class_id=args.class_id, name=args.homework_name,
                            upload_time=upload_time, deadline=deadline, homework_info=args.homework_info)
        from backend import db

        cnt = 1
        for a_problem in problem_set:
            new_homework_problem = Homework_problem(
                homework_id=homework.query.count()+1, problem_id=a_problem, sequence=cnt)
            cnt += 1
            db.session.add(new_homework_problem)
            students = Class_user.query.filter_by(class_id=args.class_id).all()
            for student in students:
                new_homework_problem_status = Homework_problem_status(homework_id=Homework.query.count(
                )+1, problem_id=a_problem, user_id=student.user_id, hand_in_status=0)
                db.session.add(new_homework_problem_status)

        db.session.add(homework)
        db.session.commit()
        return jsonify({'message': "success to add homework", 'code': 300})


class homework(Resource):
    def get(self, homework_id):
        homework = Homework.query.filter_by(homework_id=homework_id).first()
        if homework == None:
            return jsonify({'message': "homework is not found", 'code': 404})
        homework_problem = Homework_problem.query.filter_by(
            homework_id=homework_id).all()
        ret = {}
        ret["class_id"] = homework.class_id
        ret["name"] = homework.name
        ret["upload_time"] = homework.upload_time
        ret["deadline"] = homework.deadline
        ret["homework_info"] = homework.homework_info
        ret["problem_set"] = []
        for a_problem in homework_problem:
            problem = Problem.query.filter_by(
                problem_id=a_problem.problem_id).first()
            ret["problem_set"].append({'sequence':a_problem.sequence,'problem_name':problem.name,'problem_id':problem.problem_id})
        return jsonify(ret)

class homework_status(Resource):
    def get(self, homework_id):
        homework = Homework.query.filter_by(homework_id=homework_id).first()
        students = Class_user.query.filter_by(class_id=homework.class_id).all()
        if homework == None:
            return jsonify({'message': "homework is not found", 'code': 404})
        homework_problem = Homework_problem.query.filter_by(
            homework_id=homework_id).all()
        ret = {}
        ret["class_id"] = homework.class_id
        ret["name"] = homework.name
        ret["status_table"] = []
        for student in students:
            a_student_status = {}
            a_student_status['student_id'] = student.student_id
            a_student_status['status'] = []
            for a_problem in homework_problem:
                problem = {}
                problem["sequence"]=a_problem.sequence
                homework_problem_status = Homework_problem_status.query.filter_by(
            homework_id=homework.homework_id, problem_id=a_problem.problem_id, user_id=student.user_id).first()
                problem["status"]=homework_problem_status.hand_in_status
                a_student_status['status'].append(problem)
                
            ret["status_table"].append(a_student_status)
        return jsonify(ret)

class exam_table(Resource):
    def get(self,class_id):
        exams = Exam.query.filter_by(class_id=class_id).order_by(Exam.exam_id).all()
        ret = []
        for exam in exams:
            a_exam = {}
            a_exam["exam_id"] = exam.id
            a_exam["name"] = exam.name
            a_exam["start_time"] = exam.start_time.strftime("%Y/%m/%d %H:%M:%S")
            a_exam["end_time"] = exam.end_time.strftime("%Y/%m/%d %H:%M:%S")
            ret.append(a_exam)
        return jsonify(ret)

class homework_table(Resource):
    def get(self,class_id):
        homeworks = Homework.query.filter_by(class_id=class_id).order_by(Homework.homework_id).all()
        ret = []
        for homework in homeworks:
            a_homework = {}
            a_homework["homework_id"] = homework.id
            a_homework["name"] = homework.name
            a_homework["upload_time"] = homework.upload_time.strftime("%Y/%m/%d %H:%M:%S")
            a_homework["deadline"] = homework.deadline.strftime("%Y/%m/%d %H:%M:%S")
            ret.append(a_homework)
        return jsonify(ret)