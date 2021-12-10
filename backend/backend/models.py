from flask.json import jsonify, dumps
from backend import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
import base64

relations = db.Table(
    'relations between problem and topic',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.topic_id')),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.problem_id'))  
)
#✔

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
def load_user_from_header(header_val):
    header_val = header_val.replace('Basic', '', 1)
    try:
        header_val = base64.b64decode(header_val)
    except TypeError:
        pass
    return User.query.filter_by(user_id = header_val).first()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)
    #時間由API傳入時給予，非採用資料庫Default
    #python 做法
        #若引用import datetime
        #utc = datetime.datetime.now()
        #time_range = datetime.timedelta(hours = 8)
        #utc8 = utc + time_range
        #upload_date = datetime.datetime.now()+datetime.timedelta(hours = 8)
        
        #若引用from datetime import datetime
        #utc = datetime.now()
        #time_range = timedelta(hours = 8)
        #utc8 = utc + time_range
    authority = db.Column(db.Integer, default=0)
    user_to_problem = db.relationship("User_problem", backref="user")
    
    def __repr__(self):
        return jsonify({"name":self.name, "email":self.email, "register_date":str(self.register_date), "user_problem":dumps(self.user_to_problem.problem_id)})
    #def as_dict(self):
       #return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
#✔

class Problem(db.Model):
    __tablename__ = "problem"
    problem_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    questioner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(524288), nullable=False)
    time_limit = db.Column(db.Integer, nullable = False)
    memory_limit = db.Column(db.Integer, nullable = False)
    testcase_count = db.Column(db.Integer, nullable = False)
    sample_input = db.Column(db.String(1024), nullable = False)
    is_hidden = db.Column(db.Integer, nullable=False, default=0)
    upload_date = db.Column(db.DateTime, nullable=False)

    correct_source_code = db.Column(db.String(524288), nullable=False)

    #upload_date做法同上
    problem_to_user = db.relationship("User_problem", backref="problem")
    problem_topics = db.relationship("Topic", secondary=relations, backref="Problem")

    def __repr__(self):
        return f"Problem('{self.problem_id}', '{self.name}', '{self.problem_content}', '{self.difficulty}')"
#✔

class Problem_Testcase(db.Model):
    __tablename__ = "problem_testcase"
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id),nullable=False)
    testcase_id = db.Column(db.Integer, nullable=False)
    input_name = db.Column(db.String(1024),nullable=False)
    output_name = db.Column(db.String(1024),nullable=False)


class User_problem(db.Model):
    __tablename__ = "user_problem"
    user_problem_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id))
    status = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return jsonify(self.problem_id)

#✔



class Topic(db.Model):
    __tablename__ = "topic"
    topic_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(30), unique=True, nullable=False)
    topic_problems = db.relationship("Problem", secondary=relations, backref="Topic")

    def __repr__(self):
         return jsonify(self.topic_id, self.topic_name)

#✔


class Submission(db.Model):
    __tablename__ = "submission"
    submission_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    source_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    error_hint = db.Column(db.Integer)              
    error_line = db.Column(db.Integer)              
    language = db.Column(db.String(20), nullable=False)
    time_used = db.Column(db.String(20), nullable=False)      
    memory_used = db.Column(db.String(20), nullable=False)     
    exam_id = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    upload_date = db.Column(db.String(30), nullable=False)
    #同register_date做法
    code_content = db.Column(db.String(524288), nullable=False)

    def __repr__(self):
        return jsonify(self.submission_id, self.user_id, self.problem_id, self.status,self.error_hint, self.error_line, self.time_used, self.memory_used, self.exam_id, self.homework_id, str(self.upload_date), self.code_content)
#✔
    
class Queue(db.Model):
    __tablename__ = "queue"
    source_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    mode = db.Column(db.Integer, nullable=False, default=0)
    exam_id = db.Column(db.Integer)      
    homework_id = db.Column(db.Integer)  
    language = db.Column(db.String(20), nullable=False)
    upload_date = db.Column(db.String(30), nullable=False)
    #同register_date做法
    code_content = db.Column(db.String(524288), nullable=False)
    
    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    def __repr__(self):
        return jsonify(self.source_id, self.user_id, self.problem_id, self.mode, self.exam_id, self.homework_id, self.language, str(self.upload_date), self.code_content)
#✔


class Class(db.Model):
    __tablename__ = "class"
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(30), nullable=False)
    is_public = db.Column(db.Integer, default=0, nullable=False)
    invite_code = db.Column(db.Integer, nullable=False)
    #可用以下方是產生邀請碼
    # import random, string
    # s = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
    # print s
    teacher_id = db.Column(db.Integer, nullable=False)
    #此行看需不需要
    
    
class Class_user(db.Model):
    __tablename__ = "class_user"
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey(Class.class_id), nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    #這邊的student_id是否有與id重複之嫌
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    authority = db.Column(db.Integer, nullable=False, default=0)
    
class Homework(db.Model):
    __tablename__ = "homework"
    homework_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey(Class.class_id), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    uploadtime = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    
class Homework_problem(db.Model):
    __tablename__ = "homework_problem"
    id = db.Column(db.Integer, primary_key=True)
    homework_id = db.Column(db.Integer, db.ForeignKey(Homework.homework_id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    hand_in_status = db.Column(db.Integer, nullable=False, default=0)
    
class Exam(db.Model):
    __tablename__ = "exam"
    exam_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey(Class.class_id), nullable=False)
    #hackmd 內寫p.k.是否有誤
    name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    exam_detail = db.Column(db.String(), )
    #大小
class Exam_problem(db.Model):
    __tablename__ = "exam_problem"
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exam.exam_id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    sequence = db.Column(db.Integer)
    #id同?
class Dashboard(db.Model):
    __tablename__ = "dashboard"
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exam.exam_id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    try_count = db.Column(db.Integer, nullable=False)
    current_status = db.Column(db.Integer, nullable=False, default=0)
    penalty_time = db.Column(db.Integer, nullable=False, default=0)
    solved_count = db.Column(db.Integer, nullable=False, default=0)
    total_time = db.Column(db.Integer, nullable=False, default=0)