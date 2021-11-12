from multiprocessing import Process, Pool
import os,time,subprocess
import requests,json
import threading

def checking_compile_result(Source_id) :
	if os.stat("compile/%s.log"%(Source_id)).st_size != 0 :
		f = open("compile/%s.log"%(Source_id),"r")
		return "CE",f.read()
	else :
		return "AC",""

def running_func(running_case):
	Mode = int(running_case["Mode"])
	Source_id = running_case["Source_id"]
	Time_limit = running_case["Time_limit"]
	Memory_limit = running_case["Memory_limit"]
	Language = running_case["Language"]
	Test_case_name = running_case["Test_case_name"]
	if Mode == 1 :
		Problem_id = running_case["Problem_id"]
		Test_case_answer_name = running_case["Test_case_answer_name"]
		if Language == "c++" :
			subprocess.run(["docker run -i --rm -v /home/piggy/Final/Dispatch:/home/piggy/Final/Dispatch runner bash -c \" { time exe/%s </home/piggy/Final/Dispatch/test_case/%s/%s 1>/home/piggy/Final/Dispatch/finish/%s/%s.out 2>/home/piggy/Final/Dispatch/finish/%s/%s.err ; } 2>/home/piggy/Final/Dispatch/finish/%s/%s.time \" "%(Source_id,Problem_id,Test_case_name,Source_id,Test_case_name,Source_id,Test_case_name,Source_id,Test_case_name)],shell=True)
		Compare_result = ""	
		Compare_result = compare_func("/home/piggy/Final/Dispatch/finish/%s/%s.out","/home/piggy/Final/Dispatch/Answer/%s/%s")
		Time = check_time("/home/piggy/Final/Dispatch/finish/%s/%s.time")
		Memory = check_memory("/home/piggy/Final/Dispatch/finish/%s/%s.memory")
		

		

	return {"Source_id":Source_id,"Time":"1","Memory":"100","Status":"AC"}

if __name__ == "__main__" :
	requirement = requests.get("http://127.0.0.1:8000")
	req_json = json.loads(requirement.text)

	Submission_count = int(req_json['Submission_Count'])
	result = {"Return_count":Submission_count,"Return_Set":{}}
	running_case = []
	for i in range (0,Submission_count):

		Mode = int(req_json["Submission_Set"][i]["Mode"])

		Problem_id = -1
		if Mode != 3:
			Problem_id = req_json["Submission_Set"][i]["Problem_id"]

		Source_id = req_json["Submission_Set"][i]["Source_id"]

		Test_case_count = int(req_json["Submission_Set"][i]["Test_case_count"])

		Time_limit = req_json["Submission_Set"][i]["Time_limit"]

		Memory_limit = req_json["Submission_Set"][i]["Memory_limit"]

		Language = req_json["Submission_Set"][i]["Language"]

		# More Language
		if Language == "c++" :
			subprocess.run(["g++ source/%s -o exe/%s 2>compile/%s.log"%(Source_id,Source_id,Source_id)],shell=True)
		elif Language == "c" :
			subprocess.run(["gcc source/%s -o exe/%s 2>compile/%s.log"%(Source_id,Source_id,Source_id)],shell=True)
		elif Language == "python" :
			subprocess.run(["cp source/%s exe/%s"%(Source_id,Source_id)],shell=True)

		Status = "AC"
		Compile_error_out=""
		Status , Compile_error_out = checking_compile_result(Source_id)

		result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":Status,"Compile_error_out":Compile_error_out,"Time":"-1","Memory":"-1","All_stander_out":[],"All_compare_out":[]}})

		if Status == "CE" :
			continue

		if Mode == 1 :
			for j in range (0,Test_case_count):
				Test_case_name=req_json["Submission_Set"][i]["All_test_case_general_submission"][j]["Test_case_name"]
				Test_case_answer_name=req_json["Submission_Set"][i]["All_test_case_general_submission"][j]["Test_case_answer_name"]
				running_case.append({"Mode":Mode,"Problem_id":Problem_id,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Test_case_name":Test_case_name,"Test_case_answer_name":Test_case_answer_name})

		if Mode == 2 :
			Correct_source_code = req_json["Submission_Set"][i]["Correct_source_code"]
			Test_case_name = req_json["Submission_Set"][i]["All_test_case_general_submission"][0]["Test_case_name"]
			running_case.append({"Mode":Mode,"Problem_id":Problem_id,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Correct_source_code":Correct_source_code,"Test_case_name":Test_case_name})
		
		if Mode == 3 :
			for j in range (0,Test_case_count):
				Test_case_name=req_json["Submission_Set"][i]["All_test_case_general_submission"][j]["Test_case_name"]
				running_case.append({"Mode":Mode,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Test_case_name":Test_case_name})


	# threads = []
	# for i in range (0,len(running_case)) :
	# 	threads.append(threading.Thread(target = running_func, args = (running_case[i],)))
	# 	threads[i].start()

	# for i in range (0,len(running_case)) :
	# 	threads[i].join()

	# print("Done")

	pool = Pool()
	running_reslut = pool.map(running_func,running_case)

	for i in range (0,len(running_reslut)) :
		Source_id = running_reslut[i]["Source_id"]
		for key, value in running_reslut[i].items() :
			if key == "Source_id" :
				continue
			if key == "Status" and value != "AC":
				result["Return_Set"][Source_id][key] = value
			elif key == "Time" or key == "Memory" :
				preverious = int(result["Return_Set"][Source_id][key])
				current = int(value)
				result["Return_Set"][Source_id][key] = max(preverious,current)
			elif key == "All_stander_out" :
				result["Return_Set"][Source_id][key].append(value)
			elif key == "All_compare_out" :
				result["Return_Set"][Source_id][key].append(value)

	print(result["Return_Set"])





	# subprocess.run(["g++ source/main.cpp -o main 1>finish/compile_stdout.log 2>finish/compile_stderr.log"],shell=True)
	# inputs = []
	# for i in range(1,20):
	# 	inputs.append({"test_case":"1.txt","stdout":str(i)+".txt","stderr":str(i)+".txt"})
	# pool=Pool()
	# pool_outputs=pool.map(main_map,inputs)
	# pool.close()
	# pool.join()
	# print(pool_outputs)