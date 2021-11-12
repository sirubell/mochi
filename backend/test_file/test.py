from app import db
from app import User, Problem, Topic, User_problem, Submission, Queue
from fuction import add_submission, delete_submission, refresh_submission_status, add_queue, delete_queue_and_get_data, add_problem_topic, delete_problem_topic, new_user, delete_user_problem, new_problem, delete_problem, show_user_problem, show_problem_submission, show_user_submission, show_problem_set
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
db.session.commit()