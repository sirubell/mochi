from flask_restful import Api, Resource, reqparse

problem_post_args = reqparse.RequestParser()
problem_post_args.add_argument("questioner_id",type=int,required=True,help='questioner_id is required!')
problem_post_args.add_argument("name",type=str,required=True,help='name is required!')
problem_post_args.add_argument("difficulty",type=int,required=True,help='difficulty is required!')
problem_post_args.add_argument("topic",type=str)
problem_post_args.add_argument("content",type=str,required=True,help='content is required!')
problem_post_args.add_argument("time_limit",type=int,required=True,help='time_limit is required!')
problem_post_args.add_argument("memory_limit",type=int,required=True,help='memory_limit is required!')
problem_post_args.add_argument("is_hidden",type=int,required=True,help='is_hidden is required!')

problem_get_args = reqparse.RequestParser()
problem_get_args.add_argument("page",type=int,required=True,help='page is required!')



class problem(Resource):
    def get(self,page,name,difficulty,topic):
        return {"string":"Hello_world","name":name,"page":page,"difficulty":difficulty,"topic":topic}

    def post(self):
        problem = problem_post_args.parse_args()
        from models import Problem
        new_problem = Problem(questioner_id=problem.questioner,problem_name=problem.name,difficulty=problem.difficulty,topic=problem.topic,problem_content=problem.content,time_limit=problem.time_limit,memory_limit=problem.memory_limit,is_hidden=problem.is_hidden)
        from app import db
        db.session.add(new_problem)
        db.session.commit()
        return 200



