from flask_restful import reqparse
import datetime

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


signup_post_args = reqparse.RequestParser()
signup_post_args.add_argument("name", type=str, required=True, help='Username is necessary!')
signup_post_args.add_argument("email", type=str, required=True, help='Email is necessary!')
signup_post_args.add_argument("password", type=str, required=True, help='Password is necessary!')
signup_post_args.add_argument("confirm_password", type=str, required=True, help='Confirm_password is necessary!')

login_post_args = reqparse.RequestParser()
login_post_args.add_argument("email", type=str, required=True, help='Email is necessary!')
login_post_args.add_argument("password", type=str, required=True, help='Password is necessary!')

user_profile_get_args = reqparse.RequestParser()
user_profile_get_args.add_argument("name", type=str)
user_profile_get_args.add_argument("email", type=str)
user_profile_get_args.add_argument("user_to_problem", type=str)

user_profile_put_args = reqparse.RequestParser()
user_profile_put_args.add_argument("name", type=str)
user_profile_put_args.add_argument("email", type=str)
user_profile_put_args.add_argument("password", type=str)

submission_post_args = reqparse.RequestParser()
submission_post_args.add_argument("user_id", type=int, required=True, help="User_id is required!")
submission_post_args.add_argument("problem_id", type=int, required=True, help="Problem_id is required!")
submission_post_args.add_argument("source_id", type=int, required=True, help="Source_id is required!")
submission_post_args.add_argument("status", type=int, required=True, help="Status is required!")
submission_post_args.add_argument("error_hint", type=int)
submission_post_args.add_argument("error_line", type=int)
submission_post_args.add_argument("language", type=str, required=True, help="Language is required!")
submission_post_args.add_argument("time_used", type=str, required=True, help="Time_used is required!")
submission_post_args.add_argument("memory_used", type=str, required=True, help="Memory_used is required!")
submission_post_args.add_argument("exam_id", type=int)
submission_post_args.add_argument("homework_id", type=int)
submission_post_args.add_argument("code_content", type=str, required=True, help="Code_content is required!")


queue_post_args = reqparse.RequestParser()
queue_post_args.add_argument("user_id", type=int, required=True, help="User_id is required!")
queue_post_args.add_argument("problem_id", type=int, required=True, help="Problem_id is required!")
queue_post_args.add_argument("mode", type=int)
queue_post_args.add_argument("exam_id", type=int)
queue_post_args.add_argument("homework_id", type=int)
queue_post_args.add_argument("language", type=str, required=True, help="Language is required!")
queue_post_args.add_argument("status", type=int, required=True, help="Status is required!")
queue_post_args.add_argument("code_content", type=str, required=True, help="Code_content is required!")
