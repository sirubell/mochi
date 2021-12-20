from app import db
from models import User, Problem, Topic, User_problem, Submission, Queue
import json


def main():
    db.drop_all()
    db.create_all()
    user_1 = User(user_name='a', email='a@email.com', password='123')
    user_2 = User(user_name='b', email='b@email.com', password='123')
    user_3 = User(user_name='c', email='c@email.com', password='123')
    problem_1 = Problem(problem_name='problem1',
                        problem_content='1', difficulty=3)
    problem_2 = Problem(problem_name='problem2',
                        problem_content='2', difficulty=2)
    problem_3 = Problem(problem_name='problem3',
                        problem_content='3', difficulty=1)
    user_problem_1 = User_problem(user_id=1, problem_id=1, status=0)
    user_problem_2 = User_problem(user_id=1, problem_id=2, status=3)
    user_problem_3 = User_problem(user_id=1, problem_id=3, status=3)
    user_problem_4 = User_problem(user_id=2, problem_id=1, status=4)
    user_problem_5 = User_problem(user_id=2, problem_id=2, status=5)
    user_problem_6 = User_problem(user_id=2, problem_id=3, status=5)
    user_problem_7 = User_problem(user_id=3, problem_id=1, status=1)
    user_problem_8 = User_problem(user_id=3, problem_id=2, status=2)
    user_problem_9 = User_problem(user_id=3, problem_id=3, status=3)
    topic1 = Topic(topic_id=1, topic_name='tp1')
    topic2 = Topic(topic_id=2, topic_name='tp2')
    topic3 = Topic(topic_id=3, topic_name='tp3')
    db.session.add_all([user_1, user_2, user_3, problem_1, problem_2, problem_3, user_problem_1,
                        user_problem_2, user_problem_3, user_problem_4, user_problem_5, user_problem_6, user_problem_7, user_problem_8, user_problem_9, topic1, topic2, topic3])
    db.session.commit()

    new_user('d', 'd@email.com', "123")
    new_problem('problem4', '4', 4)
    add_problem_topic(1, 'tp1')
    add_problem_topic(2, 'tp2')
    add_problem_topic(3, 'tp3')
    add_queue(1, 1, 1, "XD")
    now_submission = delete_queue_and_get_data(1)
    refresh_submission_status(now_submission, 2)
    add_submission(now_submission)


def add_submission():
    # with open("out.json",mode = "r") as queue:
    # tmp = {
    #     'submission_id': submission_id
    #     'std_out': std_out
    #     'std_err': std_err
    #     'memory_usage': memory_usage
    #     'time_usage': time_usage
    # }
    tmp_submission = Submission(submission_id=queue[submission_id], user_id=queue[user_id], problem_id=queue[problem_id],
                                status=queue[status], submission_date=queue[submission_date], code_content=queue[code_content])
    db.session.add(tmp_submission)
    db.session.commit()


def delete_submission(submission_id):
    query = Submission.query.filter_by(submission_id=submission_id).first()
    db.session.delete(query)
    db.session.commit()


def refresh_submission_status(submission, new_status):
    submission.status = new_status
    return submission


def add_queue(user_id, problem_id, status, code_content):
    tmp_queue = Queue(submission_id=Queue.query.count()+Submission.query.count()+1, user_id=user_id,
                      problem_id=problem_id, status=status, code_content=code_content)
    db.session.add(tmp_queue)
    db.session.commit()


def delete_queue_and_get_data():
    query = Queue.query.filter_by(
        submission_id=Submission.query.count()+1).first()
    db.session.delete(query)
    db.session.commit()
    # with open("in.json",mode = "w") as file:
    # tmp = {
    #     'submission_id': submission_id
    #     'std_out': std_out
    #     'std_err': std_err
    #     'memory_usage': memory_usage
    #     'time_usage': time_usage
    # }
    # json.dump(tmp,file)
    # user_id, problem_id, time_limit, memory_limit, languege, code


def add_problem_topic(problem_id, topic_name):
    problem_query = Problem.query.filter_by(problem_id=problem_id).first()
    topic_query = Topic.query.filter_by(topic_name=topic_name).first()
    if(topic_query == None):
        tmp_topic = Topic(topic_name=topic_name)
        db.session.add(tmp_topic)
    problem_query.problem_topics.append(topic_query)
    db.session.commit()


def delete_problem_topic(problem_id, topic_name=None):
    problem_query = Problem.query.filter_by(problem_id=problem_id).first()
    if(topic_name == None):
        problem_query.problem_topics.clear()
    else:
        problem_topic_query = problem_query.problem_topics.query.filter_by(
            topic_name=topic_name).first()
        db.delete(problem_topic_query)
    db.session.commit()


def new_user(user_name, email, password):
    tmp_user = User(user_name=user_name, email=email, password=password)
    db.session.add(tmp_user)
    for pid in range(1, Problem.query.count()+1):
        tmp_user_problem = User_problem(
            user_id=tmp_user.user_id, problem_id=pid, status=0)
        db.session.add(tmp_user_problem)
    db.session.commit()


def delete_user_problem(problem_id):
    problem_query = Problem.query.filter_by(problem_id=problem_id).delete()
    for uid in range(1, User.query.count()+1):
        user_problem_query = User_problem.query.filter_by(
            user_id=uid, problem_id=problem_id).first()
        db.session.delete(user_problem_query)
    db.session.commit()


def new_problem(problem_name, problem_content, difficulty):
    tmp_problem = Problem(problem_name=problem_name,
                          problem_content=problem_content, difficulty=difficulty)
    db.session.add(tmp_problem)
    for uid in range(1, User.query.count()+1):
        tmp_user_problem = User_problem(
            user_id=uid, problem_id=tmp_problem.problem_id, status=0)
        db.session.add(tmp_user_problem)
    db.session.commit()


def delete_problem(problem_id):
    problem_query = Problem.query.filter_by(problem_id=problem_id).first()
    delete_problem_topic(problem_id)
    delete_user_problem(problem_id)
    db.session.delete(problem_query)
    db.session.commit()


def show_user_problem(user_id):
    tmp_user = User.query.filter_by(user_id=user_id)
    for problem in Problem.query:
        status = User_problem.query.filter_by(
            user_id=user_id, problem_id=problem.problem_id).first().status
        print(problem.problem_id, problem.problem_name, status)


def show_problem_submission(problem_id, user_id=-1, AC=False):
    if user_id == -1:
        if AC:
            submission_query = Submission.query.filter_by(
                problem_id=problem_id, status=1)
            for submission in submission_query:
                print(submission)
        else:
            queue_query = Queue.query.filter_by(problem_id=problem_id)
            for queue in queue_query:
                print(queue)
            submission_query = Submission.query.filter_by(
                problem_id=problem_id)
            for submission in submission_query:
                print(submission)
    else:
        if AC:
            submission_query = Submission.query.filter_by(
                problem_id=problem_id, user_id=user_id, states=1)
            for submission in submission_query:
                print(submission)
        else:
            queue_query = Queue.query.filter_by(
                problem_id=problem_id, user_id=user_id)
            for queue in queue_query:
                print(queue)
            submission_query = Submission.query.filter_by(
                problem_id=problem_id, user_id=user_id)
            for submission in submission_query:
                print(submission)


def show_user_submission(user_id, AC=False):
    if AC:
        submission_query = Submission.query.filter_by(
            user_id=user_id, states=1)
        for submission in submission_query:
            print(submission)
    else:
        queue_query = Queue.query.filter_by(user_id=user_id)
        for queue in queue_query:
            print(queue)
        submission_query = Submission.query.filter_by(user_id=user_id)
        for submission in submission_query:
            print(submission)


def show_problem_set(user_id=-1):
    if user_id == -1:
        for problem in Problem.query:
            print(problem)
    else:
        for user_problem in User_problem.query:
            print(user_problem.problem+user_problem.status)


main()
