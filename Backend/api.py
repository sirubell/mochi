from flask_restful import Api, Resource, reqparse
# from app import db
# from models import Problem



problem_post_args = problem_post_args = reqparse.RequestParser()
problem_post_args.add_argument("questioner_id",type=int,required=True)
problem_post_args.add_argument("name",type=str,required=True)
problem_post_args.add_argument("difficulty",type=int,required=True)
problem_post_args.add_argument("topic",type=str)
problem_post_args.add_argument("content",type=str,required=True)
problem_post_args.add_argument("time_limit",type=int,required=True)
problem_post_args.add_argument("memory_limit",type=int,required=True)
problem_post_args.add_argument("is_hidden",type=int,required=True)




