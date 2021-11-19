from app import db
from models import User, Problem, Topic, User_problem, Submission, Queue
# from fuction import add_submission, delete_submission, refresh_submission_status, add_queue, delete_queue_and_get_data, add_problem_topic, delete_problem_topic, new_user, delete_user_problem, new_problem, delete_problem, show_user_problem, show_problem_submission, show_user_submission, show_problem_set
db.drop_all()
db.create_all()
db.session.commit()