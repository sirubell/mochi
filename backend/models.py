from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)
    #時間由API傳入時給予，非採用資料庫Default
    #python 做法
        #若引用from datetime import datetime
        #utc = datetime.datetime.now()
        #time_range = datetime.timedelta(hours = 8)
        #utc8 = utc + time_range
        
        #若未引用from datetime import datetime
        #utc = datetime.now()
        #time_range = timedelta(hours = 8)
        #utc8 = utc + time_range
    authority = db.Column(db.Integer, default=0)
    user_to_problem = db.relationship("User_problem", backref="user")

    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}')"
#✔

class Problem(db.Model):
    __tablename__ = "problem"
    problem_id = db.Column(db.Integer, primary_key=True)
    problem_name = db.Column(db.String(128), unique=True, nullable=False)
    questioner_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(524288), nullable=False)
    time_limit = db.Column(db.Integer, nullable = True)
    memory_limit = db.Column(db.Integer, nullable = True)
    testcase_count = db.Column(db.Integer, nullable = False)
    sample_input = db.Column(db.String(1024), nullable=False)
    is_hidden = db.Column(db.Integer, nullable=False, default=0)
    upload_date = db.Column(db.DateTime, nullable=False)
    #upload_date做法同上
    problem_to_user = db.relationship("User_problem", backref="problem")
    #problem_topics = db.relationship("Topic", secondary=relations, backref="Problem")

    def __repr__(self):
        return f"Problem('{self.problem_id}', '{self.problem_name}', '{self.problem_content}', '{self.difficulty}')"
#!

class User_problem(db.Model):
    __tablename__ = "user_problem"
    user_problem_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id))
    status = db.Column(db.Integer, nullable=False, default=0)

#✔

relations = db.Table(
    'relations',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.topic_id')),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.problem_id'))  
)
#✔

class Topic(db.Model):
    __tablename__ = "topic"
    topic_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(30), unique=True, nullable=False)
    #topic_problems = db.relationship("Problem", secondary=relations, backref="Topic")

    def __repr__(self):
        return f"Topic('{self.topic_id}', '{self.topic_name}')"
#!



class Submission(db.Model):
    __tablename__ = "submission"
    submission_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    source_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    # error_hint = db.Column(db.Integer)              # storage mode
    # error_line = db.Column(db.Integer)              # storage mode
    language = db.Column(db.String(20), nullable=False)
    time_used = db.Column(db.String(20), nullable=False)      
    Memory_used = db.Column(db.String(20), nullable=False)     
    exam_id = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    upload_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    code_content = db.Column(db.String(524288), nullable=False)

    def __repr__(self):
        return f"Submission('{self.submission_id}', '{self.user_id}', '{self.problem_id}', '{self.status}', '{self.code_content}')"

class Queue(db.Model):
    __tablename__ = "queue"
    source_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey(Problem.problem_id), nullable=False)
    mode = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #utc is American time!!
    #exam_id = db.Column(db.Integer, nullable=False)      # is_nullable
    #homework_id = db.Columm(db.Integer, nullable=False)  # is_nullable
    code_content = db.Column(db.String(524288), nullable=False)
    languege = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Queue('{self.submission_id}', '{self.user_id}', '{self.problem_id}', '{self.status}', '{self.code_content}','{self.languege}')"

#!