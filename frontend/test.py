from flask import Flask,request
import json

app=Flask(__name__)

# {
#     //notation [] : Which mode will have this value
#     //How much submission in this query
#     // ? = number
#     "Submission_Count":"?"
#     //Detail of each submission
#     "Submission_Set":
#     [
#         //How many submission we get then we will have corresponding dictionary
#         {
#             //The mode of this submission [1,2,3]
#             // 1. General Submission
#             // 2. Test Run
#             // 3. Create New Question
#             // ? = number
#             "Mode":"?"
#             //The id of this problem [1,2]
#             // ? = string
#             "Problem_id":"?"
#             //Source id [1,2,3]
#             // ? = string
#             "Source_id":"?"
#             //How much test case does this problem have [1,3]
#             // ? = number
#             "Test_case_count":"?"
#             //How much time it can take [1,2,3]
#             // ? = number
#             "Time_limit":"?"
#             //How much memory it can take [1,2,3]
#             // ? = number
#             "Memory_limit":"?"
#             //The language of source code [1,2,3]
#             // ? = string
#             "Language":"?"
#             //The correct source code of this problem [2]
#             // ? = string
#             "Correct_source_code":"?"
#             //We will need the test case file name and the answer of this test case answer file name [1]
#             "All_test_case_general_submission":
#             [
#                 //How many test case does this question have then we will have corresponding dictionary
#                 // ? = string
#                 {"Test_case_name":"?","Test_case_answer_name":"?"}
#             ]
#             //We will need all in put file [2,3]
#             "Self_test_case":
#             [
#                 //How many test case does this question have then we will have corresponding dictionary
#                 // ? = string
#                 {"Test_case_name":"?"}
#             ]
#         }
#     ]
# }

@app.route('/')
def main():
	res={
        [
            {"stuId":1,"stuName":"李華","stuSex":"男","stuAge":20},
            {"stuId":2,"stuName":"張國偉","stuSex":"男","stuAge":22},
            {"stuId":3,"stuName":"劉豔","stuSex":"女","stuAge":19},
            {"stuId":4,"stuName":"李小燕","stuSex":"女","stuAge":22},
            {"stuId":5,"stuName":"張鵬","stuSex":"男","stuAge":26},
            {"stuId":6,"stuName":"李曄","stuSex":"女","stuAge":20},
            {"stuId":7,"stuName":"錢國強","stuSex":"男","stuAge":21},
            {"stuId":8,"stuName":"張三","stuSex":"男","stuAge":22},
            {"stuId":9,"stuName":"唐毓民","stuSex":"男","stuAge":25},
            {"stuId":10,"stuName":"瑪麗亞","stuSex":"女","stuAge":21},
            {"stuId":11,"stuName":"李家明","stuSex":"男","stuAge":21}
        ]
	}
	return json.dumps(res)

if __name__=="__main__":
	app.run(host="127.0.0.1",port=8000)