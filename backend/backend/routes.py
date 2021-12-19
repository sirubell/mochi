from flask import jsonify, url_for, redirect, flash, render_template, request
from flask_login.utils import login_required
from flask_restful import Api, Resource, abort
import datetime
from backend.exception import if_email_has_existed, if_username_has_existed, if_problemname_has_existed, is_email_format, confirm_password_equal_password
from backend.models import Homework, Problem, User, Submission, User_problem, Queue, Problem_Testcase
from backend import bcrypt,BASE
from backend.argument import signup_post_args, submission_post_args, login_post_args, user_profile_put_args, problem_post_args, problem_put_args, problem_get_args, queue_post_args, dispatcher_post_args, test_run_post_args, create_problem_test_run_args
from flask_login import login_user, current_user, logout_user, login_required
import os

from backend import app




class check(Resource):
    def get(self):
        return os.path.abspath(os.path.dirname(__file__))


class delete_dir(Resource):
    def delete(self):
        import shutil
        shutil.rmtree(BASE+'buffer')
        os.mkdir(BASE+'buffer')
        if os.path.isdir(BASE+"Problem"):
            shutil.rmtree(BASE+'Problem')
            os.mkdir(BASE+'Problem')
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
            page = request.args['page']
        else:
            return "Error, page is required"
        topic = None
        difficulty = None
        name = None
        if 'topic' in request.args:
            topic = request.args['topic']
        if 'difficulty' in request.args:
            difficulty = request.args['difficulty']
        if 'name' in request.args:
            name = request.args['name']

        problems = Problem.query.all()
        ''' if topic and difficulty and name:
            from backend import db
            problems = Problem.query.filter(db.and_(db.and_(Problem.topic==topic,Problem.difficulty==difficulty),Problem.name.like(name))).all()
        elif topic:
            problems = Problem.query.filter(Problem.topic==topic).all()
        elif topic and difficulty:
            problems = Problem.query.filter(db.and_(Problem.difficulty==difficulty,Problem.topic==topic)).all()'''

        if difficulty:
            problems = Problem.query.filter(
                Problem.difficulty == difficulty).all()
        elif name:
            problems = Problem.query.filter(Problem.name.like(name)).all()
        elif difficulty and name:
            problems = Problem.query.filter(
                db.and_(Problem.difficulty == difficulty, Problem.name.like(name))).all()

        if problems:
            ret = {}
            ret["returnset"] = []
            for problem in problems:
                ret["returnset"].append({
                    "id": problem.problem_id,
                    "name": problem.name,
                    "difficulty": problem.difficulty
                })
            return jsonify(ret)
        return "problem is not found", 404

    def post(self):
        problem = problem_post_args.parse_args()
        if_problemname_has_existed(problem.name)
        now = Queue.query.filter_by(source_id=problem.source_id).first()
        new_problem = Problem(questioner_id=problem.questioner_id, name=problem.name, difficulty=problem.difficulty, content=problem.content, time_limit=problem.time_limit, memory_limit=problem.memory_limit,
                              testcase_count=now.test_case_count, sample_input=problem.sample_input, is_hidden=problem.is_hidden, upload_date=datetime.datetime.now(), correct_source_code=problem.correct_source_code, correct_answer_language=problem.correct_answer_language)

        if now.status == 0:
            return "not ok"
        if not os.path.isdir(BASE+"buffer"):
            os.mkdir(BASE+"buffer")
        path = BASE+"buffer/"+str(now.user_id)
        import shutil
        if not os.path.isdir(BASE+"Problem"):
            os.mkdir(BASE+"Problem")
        os.rename(BASE+"buffer/"+str(now.source_id)+'.ansexe', BASE+"buffer/"+str(Problem.query.count()+1)+'.ansexe')
        shutil.move(path, BASE+"Problem/"+str(Problem.query.count()+1))
        from backend import db
        for i in range(now.test_case_count):
            test_case = Problem_Testcase(problem_id=Problem.query.count(
            )+1, testcase_id=i+1, input_name=str(i+1)+'.in', output_name=str(i+1)+'.ans')
            db.session.add(test_case)
        db.session.add(new_problem)
        db.session.delete(now)
        db.session.commit()
        return "Success to add problem", 200


class create_problem_test_run(Resource):
    def get(self):
        if 'source_id' in request.args:
            source_id = request.args['source_id']
        else:
            return "Error, source_id is required"

        if 'user_id' in request.args:
            user_id = request.args['user_id']
        else:
            return "Error, user_id is required"
        now = Queue.query.filter_by(source_id=source_id).first()
        if now.status == 0:
            return "not ok"
        if not os.path.isdir(BASE+"buffer"):
            os.mkdir(BASE+"buffer")
        path = BASE+"buffer/"+str(source_id)
        res = {}
        res["test_case_count"] = now.test_case_count
        res["return_set"] = []
        for i in range(len(now.test_case_count)):
            # from backend.convert_file_to_json import convert_file_to_json as yea
            # res = yea("buffer/"+str(user.id)+"/"+str(i+1)+'.ans')
            with open(BASE+"buffer/"+str(source_id)+"/"+str(i+1)+'.ans', mode="r", encoding="utf-8") as file:
                temp = file.read()
                res["return_set"].append(temp)

        return res

    def post(self):
        args = create_problem_test_run_args.parse_args()
        if not os.path.isdir(BASE+"buffer"):
            os.mkdir(BASE+"buffer")

        input_set = args["test_case"]
        new_queue = Queue(user_id=args.user_id, mode=3, language=args.language, test_case_count=len(input_set), upload_date=str(
        datetime.datetime.now()), code_content=args.code_content)
        from backend import db
        db.session.add(new_queue)
        db.session.commit()
        path = BASE+"buffer/"+str(new_queue.source_id)
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            return "Error, XD"
        #omgomg
        with open(path+"/"+"correct_source_code"+'.'+str(args.language), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)
        cnt = 1
        for testcase in input_set:
            with open(path+'/'+str(cnt)+".in", mode='w', encoding="utf-8") as file:
                file.write(testcase)
            cnt += 1

        return 200


class test_run(Resource):
    def get(self):
        if 'source_id' in request.args:
            source_id = request.args['source_id']
        else:
            return "Error, source_id is required"
        now = Queue.query.filter_by(source_id=source_id).first()
        if now.status == 0:
            return "not ok"
        # from backend.convert_file_to_json import convert_file_to_json as yea
        # res = yea("buffer/"+str(source_id)+'.ans')
        if not os.path.isdir(BASE+"buffer"):
            os.mkdir(BASE+"buffer")
        with open(BASE+"buffer/"+str(source_id)+".ans", mode="r", encoding="utf-8") as file:
            res = file.read()
        from backend import db
        db.session.delete(now)
        db.session.commit()
        return res

    def post(self):
        from backend import db
        args = test_run_post_args.parse_args()
        if not os.path.isdir(BASE+"buffer"):
            os.mkdir(BASE+"buffer")
        new_queue = Queue(user_id=args.user_id, mode=2, problem_id=args.problem_id, language=args.language, upload_date=str(
            datetime.datetime.now()), code_content=args.code_content, test_case_count=1)
        source_id = Queue.query.count() + 1
        with open(BASE+"buffer/"+str(Queue.query.count() + 1)+".in", mode="w", encoding="utf-8") as file:
            file.write(args.test_case)
        with open(BASE+"buffer/"+str(Queue.query.count() + 1)+'.'+str(args.language), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)
        db.session.add(new_queue)
        db.session.commit()
        return 200, source_id


class problem_id(Resource):
    def get(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id).first()
        return problem.as_dict()

    def put(self, problem_id):
        args = problem_put_args.parse_args()
        problem = Problem.query.filter_by(problem_id=problem_id).first()
        if problem == None:
            return "problem_id does not exist", 500
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
        if args.sample_input:
            problem.sample_input = args.sample_input
        if args.testcase_count:
            problem.testcase_count = args.testcase_count
        if args.is_hidden:
            problem.is_hidden = args.is_hidden
        if args.correct_source_code:
            problem.correct_source_code = args.correct_source_code
        from backend import db
        db.session.commit()
        return "Success to put problem", 200

    def delete(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id).delete()
        from backend import db
        db.session.commit()
        return "Success to delete problem", 200


class problem_solution(Resource):
    def get(self, problem_id):
        problem = Problem.query.filter_by(problem_id=problem_id)
        if problem == None:
            return "problem does not exist", 404

        return problem.correct_source_code


class problem_submission(Resource):
    def get(self, problem_id, user_id=-1):
        problem = Problem.query.filter_by(problem_id=problem_id)
        if problem == None:
            return "problem does not exist", 400
        user = User.query.filter_by(user_id=user_id)
        if user == None:
            return "user does not exist", 400
        if user_id != -1:
            submissions = Submission.query.filter_by(
                **{"user_id": user_id, "problem_id": problem.problem_id}).all()
        else:
            submissions = Submission.query.filter_by(
                problem_id=problem.problem_id).all()

        if submissions:
            ret = {}
            ret["returnset"] = []
            for submission in submissions:
                ret["returnset"].append({
                    "submission_id": submission.submission_id,
                    "problem_id": problem.problem_id,
                    "name": user.name,
                    "status": submission.status,
                    "language": submission.language,
                    "upload_date": submission.upload_date
                })
            return jsonify(ret)
        return "you have not tried this problem"


class status(Resource):
    def get(self, page):
        submissions = Submission.query.all()
        ret = {}
        ret["returnset"] = []
        for submission in submissions:
            ret["returnset"].append({
                "submission_id": submission.submission_id,
                "problem_id": problem.problem_id,
                "name": User.name,
                "status": submission.status,
                "language": submission.language,
                "upload_date": submission.upload_date
            })
        return jsonify(ret)


class signup(Resource):
    def get(self):
        # return 'Signup'
        return render_template("register.html")
        # get 註冊畫面

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        args = signup_post_args.parse_args()
        if_username_has_existed(args.name)
        is_email_format(args.email)
        if_email_has_existed(args.email)
        confirm_password_equal_password(args.password, args.confirm_password)
        hashed_password = bcrypt.generate_password_hash(
            args.password).decode('utf-8')
        new_user = User(name=args.name, email=args.email,
                        password=hashed_password, register_date=datetime.datetime.now())
        # 時間這邊，我先將這個{+datetime.timedelta(hours = 8)}拿掉，用臺灣當伺服器好像就是這邊的標準時間了
        from backend import db
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You are able to log in now', 'Success')
        return redirect(url_for('login'))


class login(Resource):
    def get(self):
        return render_template('login.html')

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        args = login_post_args.parse_args()
        user = User.query.filter_by(email=args.email).first()
        if user and bcrypt.check_password_hash(user.password, args.password):
            login_user(user, remember=args.remember)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        elif user:
            # return ('Password is wrong')
            flash('Password is wrong')
            return render_template('login.html', args=args)
        else:
            abort(404, message="Couldn't find the user")


class logout(Resource):
    def logout():
        logout_user()
        return redirect(url_for('home'))

# if no login 401


class user_profile(Resource):
    def get(self, user_id):
        from backend import db
        user = User.query.filter_by(id=user_id).first_or_404()
        ACs = User_problem.query.filter_by(user_id=user.id, status=1).all()
        datas = []
        for AC in ACs:
            datas.append(AC.problem_id)
        return jsonify({"name": user.name, "email": user.email, "register_date": str(user.register_date), "user_problem": datas})

    def put(self):
        args = user_profile_put_args.parse_args()
        if_username_has_existed(args.name)
        if_email_has_existed(args.email)
        self = args
        from backend import db
        db.session.commit()


class submission_data(Resource):
    def get(self, source_id):
        from backend import db
        submission = Submission.query.filter_by(
            source_id=source_id).first_or_404()
        return submission.as_dict()


class queue_new(Resource):
    def post(self):
        from backend import db
        args = queue_post_args.parse_args()
        problem = Problem.query.filter_by(problem_id=args.problem_id).first()
        new_queue = Queue(user_id=args.user_id, problem_id=args.problem_id, mode=1, exam_id=args.exam_id,
                          homework_id=args.homework_id, language=args.language, upload_date=str(datetime.datetime.now()), code_content=args.code_content, test_case_count=problem.testcase_count)

        if not os.path.isdir(BASE+"buffer/"):
            os.mkdir(BASE+"buffer/")

        with open(BASE+"buffer/"+str(Queue.query.count() + 1)+'.'+str(args.language), mode="w", encoding="utf-8") as file:
            file.write(args.code_content)

        db.session.add(new_queue)
        db.session.commit()
        return 200


class dispatcher(Resource):
    def get(self):
        from backend import db
        from backend.convert_file_to_json import convert_file_to_json as yea
        queues = Queue.query.limit(10).all()
        datas = {}
        datas["Submission_Count"] = len(queues)
        datas["Submission_Set"] = []
        cnt = 0
        for queue in queues:
            data = {}
            data["Mode"] = queue.mode
            if queue.mode in [1, 2]:
                data["Problem_id"] = queue.problem_id
            data["Source_id"] = queue.source_id
            data["Keep"] = 1
            problem = Problem.query.filter_by(
                problem_id=queue.problem_id).first()
            if problem == None and queue.mode in [1, 2]:
                return "no problem's id = " + str(queue.problem_id)
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
                        {"Test_case_name": testcases[i].input_name.replace('.in',""), "Test_case_answer_name": testcases[i].output_name.replace('.ans',"")})

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

        return jsonify(datas)

    def post(self):
        from backend import db
        args = dispatcher_post_args.parse_args()
        count = args["Return_count"]
        for submission in args["Return_Set"]:
            data = Queue.query.filter_by(
                source_id=submission["Source_id"]).first()
            if data.mode == 1:
                new_submission = Submission(user_id=data.user_id, problem_id=data.problem_id, source_id=submission["Source_id"], status=submission["Status"], code_content=data.code_content, exam_id=data.exam_id, homework_id=data.homework_id, error_hint=submission[
                    "Compile_error_out"], error_line=0, language=data.language, time_used=submission["Time"], memory_used=submission["Memory"], upload_date=data.upload_date)
                db.session.add(new_submission)
                Queue.query.filter_by(
                    source_id=submission["Source_id"]).delete()
            elif data.mode == 2:
                data.status = 1
                if not os.path.isdir(BASE+"buffer/"):
                    os.mkdir(BASE+"buffer/")
                with open(BASE+"buffer/"+str(data.source_id)+".ans", mode="w", encoding="utf-8") as file:
                    file.write(submission["All_stander_out"][str(1)])
            else:
                data.status = 1
                if not os.path.isdir(BASE+"buffer/"+str(data.user_id)+"/"):
                    os.mkdir(BASE+"buffer/"+str(data.user_id)+"/")
                cnt = 1
                for i in range(len(submission["All_stander_out"])):
                    with open(BASE+"buffer/"+str(data.user_id)+"/"+str(cnt)+".ans", mode="w", encoding="utf-8") as file:
                        file.write(submission["All_stander_out"][str(i+1)])
                    cnt += 1
        db.session.commit()
        return "success to return", 200
