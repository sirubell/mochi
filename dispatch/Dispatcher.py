from multiprocessing import Process, Pool
import os,time,subprocess
import requests,json
import threading
import utility

file_root = os.getcwd()

def running_func(running_case):
	Mode = int(running_case["Mode"])
	Source_id = running_case["Source_id"]
	Time_limit = running_case["Time_limit"]
	Memory_limit = int(running_case["Memory_limit"])
	Language = running_case["Language"]
	Test_case_name = running_case["Test_case_name"]

	if Mode == 1 :
		Problem_id = running_case["Problem_id"]
		Test_case_answer_name = running_case["Test_case_answer_name"]

		try :
			if utility.check_file_exist("%s/Submission/%s/%s.exe"%(file_root,Source_id,Source_id)) == "Check_File_Exit_Error" :
					return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Check_File_Exit_Error","All_compare_out":{Test_case_name:"Check_File_Exit_Error"}}
			if Language == "c++" or Language == "c":
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory %s/Submission/%s/%s.exe <%s/Problem/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Problem_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
			elif Language == 'python':
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory python3 %s/Submission/%s/%s.exe <%s/Problem/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Problem_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
		except :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Running_Error","All_compare_out":{Test_case_name:"Running_Error"}}

		Runtime_Error_status = utility.check_Runtime_Error("%s/Submission/%s/%s.err"%(file_root,Source_id,Test_case_name))			
		if Runtime_Error_status == "Check_Runtime_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:Runtime_Error_status}}
		elif Runtime_Error_status != "OK" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:"RE"}}
		TLE_MLE_status = utility.check_TLE_MLE("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name),Memory_limit)
		if TLE_MLE_status == "Check_TLE_MLE_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status}}
		elif TLE_MLE_status != "OK" :
			spec_time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
			spec_memory = utility.check_spec_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))
			if spec_memory == "Check_Spec_Memory_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_memory,"All_compare_out":{Test_case_name:spec_memory}}
			elif spec_time == "Check_Time_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_time,"All_compare_out":{Test_case_name:spec_time}}
			return {"Source_id":Source_id,"Time":spec_time,"Memory":spec_memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status}}

		Time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
		Memory = utility.check_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))
		if Time == "Check_Time_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Time,"All_compare_out":{Test_case_name:Time}}
		if Memory == "Check_Memeory_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Memory,"All_compare_out":{Test_case_name:Memory}}

		if Memory > (Memory_limit*1024) : 
			TLE_MLE_status = "MLE"
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status}}

		Compare_result = ""
		Compare_result = utility.compare_func("%s/Submission/%s/%s.out"%(file_root,Source_id,Test_case_name),"%s/Problem/%s/%s.ans"%(file_root,Problem_id,Test_case_name))
		if Compare_result == "Compare_Func_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Compare_result,"All_compare_out":{Test_case_name:Compare_result}}

		return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":Compare_result,"All_compare_out":{Test_case_name:Compare_result}}

	if Mode == 2 :
		Problem_id = running_case["Problem_id"]
		Correct_source_code = running_case["Correct_source_code"]
		try :
			if utility.check_file_exist("%s/Submission/%s/%s.exe"%(file_root,Source_id,Source_id)) == "Check_File_Exit_Error" :
					return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Check_File_Exit_Error","All_compare_out":{Test_case_name:"Check_File_Exit_Error"},"All_stander_out":{Test_case_name:""}}
			if Language == "c++" or Language == "c" :
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory %s/Submission/%s/%s.exe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
			elif Language == "python":
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory python3 %s/Submission/%s/%s.exe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
		except :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Running_Error","All_compare_out":{Test_case_name:"Running_Error"},"All_stander_out":{Test_case_name:""}}

		Runtime_Error_status = utility.check_Runtime_Error("%s/Submission/%s/%s.err"%(file_root,Source_id,Test_case_name))			
		if Runtime_Error_status == "Check_Runtime_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Check_Runtime_Error","All_compare_out":{Test_case_name:"Check_Runtime_Error"},"All_stander_out":{Test_case_name:""}}
		elif Runtime_Error_status != "OK" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:"RE"},"All_stander_out":{Test_case_name:""}}

		Stander_out = utility.get_stander_out("%s/Submission/%s/%s.out"%(file_root,Source_id,Test_case_name))
		if Stander_out == "Get_Stander_Out_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Stander_out,"All_compare_out":{Test_case_name:Stander_out},"All_stander_out":{Test_case_name:""}}
		elif Stander_out == "OE" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Stander_out,"All_compare_out":{Test_case_name:Stander_out},"All_stander_out":{Test_case_name:""}}

		TLE_MLE_status = utility.check_TLE_MLE("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name),Memory_limit)
		if TLE_MLE_status == "Check_TLE_MLE_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:""}}
		elif TLE_MLE_status != "OK" :
			spec_time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
			spec_memory = utility.check_spec_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))
			if spec_memory == "Check_Spec_Memory_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_memory,"All_compare_out":{Test_case_name:spec_memory},"All_stander_out":{Test_case_name:Stander_out}}
			elif spec_time == "Check_Time_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_time,"All_compare_out":{Test_case_name:spec_time},"All_stander_out":{Test_case_name:Stander_out}}
			return {"Source_id":Source_id,"Time":spec_time,"Memory":spec_memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:Stander_out}}

		Time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
		Memory = utility.check_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))

		if Time == "Check_Time_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Time,"All_compare_out":{Test_case_name:Time},"All_stander_out":{Test_case_name:Stander_out}}
		if Memory == "Check_Memeory_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Time,"All_compare_out":{Test_case_name:Time},"All_stander_out":{Test_case_name:Stander_out}}

		if Memory > (Memory_limit*1024) : 
			TLE_MLE_status = "MLE"
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:Stander_out}}	

		Correct_answer_language = running_case["Correct_answer_language"]

		try :
			if utility.check_file_exist("%s/Problem/%s/%s.ansexe"%(file_root,Problem_id,Problem_id)) == "Check_File_Exit_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Check_File_Exit_Error","All_compare_out":{Test_case_name:"Check_File_Exit_Error"},"All_stander_out":{Test_case_name:""}}
			if Correct_answer_language == "c" or Correct_answer_language == "c++":
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.ansmemory %s/Problem/%s/%s.ansexe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.ansout 2>%s/Submission/%s/%s.anserr ; } 2>%s/Submission/%s/%s.anstime \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Problem_id,Problem_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
			elif Correct_answer_language == "python":
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.ansmemory python3 %s/Problem/%s/%s.ansexe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.ansout 2>%s/Submission/%s/%s.anserr ; } 2>%s/Submission/%s/%s.anstime \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Problem_id,Problem_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
		except :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Running_Error","All_compare_out":{Test_case_name:"Running_Error"},"All_stander_out":{Test_case_name:""}}
		
		Runtime_Error_status_answer = utility.check_Runtime_Error("%s/Submission/%s/%s.anserr"%(file_root,Source_id,Test_case_name))			
		if Runtime_Error_status == "Check_Runtime_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:Runtime_Error_status},"All_stander_out":{Test_case_name:""}}
		elif Runtime_Error_status_answer != "OK" :
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":"Input Error","All_compare_out":{Test_case_name:"Input Error"},"All_stander_out":{Test_case_name:Stander_out}}

		Stander_out_answer = utility.get_stander_out("%s/Submission/%s/%s.ansout"%(file_root,Source_id,Test_case_name))
		if Stander_out == "Get_Stander_Out_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Stander_out,"All_compare_out":{Test_case_name:Stander_out},"All_stander_out":{Test_case_name:""}}
		elif Stander_out_answer == "OE" :
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":"Input Error","All_compare_out":{Test_case_name:"Input Error"},"All_stander_out":{Test_case_name:Stander_out}}

		TLE_MLE_status_answer = utility.check_TLE_MLE("%s/Submission/%s/%s.ansmemory"%(file_root,Source_id,Test_case_name),Memory_limit)
		if TLE_MLE_status_answer == "Check_TLE_MLE_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":TLE_MLE_status_answer,"All_compare_out":{Test_case_name:TLE_MLE_status_answer},"All_stander_out":{Test_case_name:""}}
		elif TLE_MLE_status_answer != "OK" :
			spec_time_answer = utility.check_time("%s/Submission/%s/%s.anstime"%(file_root,Source_id,Test_case_name))
			spec_memory_answer = utility.check_spec_memory("%s/Submission/%s/%s.ansmemory"%(file_root,Source_id,Test_case_name))
			if spec_memory_answer == "Check_Spec_Memory_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_memory_answer,"All_compare_out":{Test_case_name:spec_memory_answer},"All_stander_out":{Test_case_name:Stander_out}}
			elif spec_time_answer == "Check_Time_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_time_answer,"All_compare_out":{Test_case_name:spec_time_answer},"All_stander_out":{Test_case_name:Stander_out}}
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":"Input Error","All_compare_out":{Test_case_name:"Input Error"},"All_stander_out":{Test_case_name:Stander_out}}

		Time_answer = utility.check_time("%s/Submission/%s/%s.anstime"%(file_root,Source_id,Test_case_name))
		Memory_answer = utility.check_memory("%s/Submission/%s/%s.ansmemory"%(file_root,Source_id,Test_case_name))

		if Time_answer == "Check_Time_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Time_answer,"All_compare_out":{Test_case_name:Time_answer},"All_stander_out":{Test_case_name:Stander_out}}
		if Memory_answer == "Check_Memeory_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Memory_answer,"All_compare_out":{Test_case_name:Memory_answer},"All_stander_out":{Test_case_name:Stander_out}}

		if Memory_answer > (Memory_limit*1024) : 
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":"Input Error","All_compare_out":{Test_case_name:"Input Error"},"All_stander_out":{Test_case_name:Stander_out}}	


		Compare_result = ""
		Compare_result = utility.compare_func("%s/Submission/%s/%s.out"%(file_root,Source_id,Test_case_name),"%s/Submission/%s/%s.ansout"%(file_root,Source_id,Test_case_name))

		if Compare_result == "Compare_Func_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Compare_result,"All_compare_out":{Test_case_name:Compare_result},"All_stander_out":{Test_case_name:""}}

		return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":Compare_result,"All_compare_out":{Test_case_name:Compare_result},"All_stander_out":{Test_case_name:Stander_out}}

	if Mode == 3 :

		try :
			if utility.check_file_exist("%s/Submission/%s/%s.exe"%(file_root,Source_id,Source_id)) == "Check_File_Exit_Error" :
					return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Check_File_Exit_Error","All_compare_out":{Test_case_name:"Check_File_Exit_Error"},"All_stander_out":{Test_case_name:""}}
			if Language == "c++" or Language == "c" :
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory %s/Submission/%s/%s.exe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
			elif Language == "python":
				subprocess.run(["docker run --ulimit cpu=%s --memory %sm -i --rm -v %s:%s runner bash -c \" { time /usr/bin/time -f \"%%M\" -o %s/Submission/%s/%s.memory python3 %s/Submission/%s/%s.exe <%s/Submission/%s/%s.in 1>%s/Submission/%s/%s.out 2>%s/Submission/%s/%s.err ; } 2>%s/Submission/%s/%s.time \" "%(Time_limit,Memory_limit,file_root,file_root,file_root,Source_id,Test_case_name,file_root,Source_id,Source_id,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name,file_root,Source_id,Test_case_name)],shell=True)
		except :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":"Running_Error","All_compare_out":{Test_case_name:"Running_Error"},"All_stander_out":{Test_case_name:""}}

		Runtime_Error_status = utility.check_Runtime_Error("%s/Submission/%s/%s.err"%(file_root,Source_id,Test_case_name))			
		if Runtime_Error_status == "Check_Runtime_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:Runtime_Error_status},"All_stander_out":{Test_case_name:""}}
		elif Runtime_Error_status != "OK" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Runtime_Error_status,"All_compare_out":{Test_case_name:"RE"},"All_stander_out":{Test_case_name:""}}

		Stander_out = utility.get_stander_out("%s/Submission/%s/%s.out"%(file_root,Source_id,Test_case_name))
		if Stander_out == "Get_Stander_Out_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Stander_out,"All_compare_out":{Test_case_name:Stander_out},"All_stander_out":{Test_case_name:""}}
		elif Stander_out == "OE" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Stander_out,"All_compare_out":{Test_case_name:"OE"},"All_stander_out":{Test_case_name:""}}

		TLE_MLE_status = utility.check_TLE_MLE("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name),Memory_limit)
		if TLE_MLE_status == "Check_TLE_MLE_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:""}}
		elif TLE_MLE_status != "OK" :
			spec_time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
			spec_memory = utility.check_spec_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))
			spec_time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
			spec_memory = utility.check_spec_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))
			if spec_memory == "Check_Spec_Memory_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_memory,"All_compare_out":{Test_case_name:spec_memory},"All_stander_out":{Test_case_name:Stander_out}}
			elif spec_time == "Check_Time_Error" :
				return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":spec_time,"All_compare_out":{Test_case_name:spec_time},"All_stander_out":{Test_case_name:Stander_out}}
			return {"Source_id":Source_id,"Time":spec_time,"Memory":spec_memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:Stander_out}}

		Time = utility.check_time("%s/Submission/%s/%s.time"%(file_root,Source_id,Test_case_name))
		Memory = utility.check_memory("%s/Submission/%s/%s.memory"%(file_root,Source_id,Test_case_name))

		if Time == "Check_Time_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Time,"All_compare_out":{Test_case_name:Time},"All_stander_out":{Test_case_name:Stander_out}}
		if Memory == "Check_Memeory_Error" :
			return {"Source_id":Source_id,"Time":-1,"Memory":-1,"Status":Memory,"All_compare_out":{Test_case_name:Memory},"All_stander_out":{Test_case_name:Stander_out}}

		if Memory > (Memory_limit*1024) : 
			TLE_MLE_status = "MLE"
			return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":TLE_MLE_status,"All_compare_out":{Test_case_name:TLE_MLE_status},"All_stander_out":{Test_case_name:Stander_out}}	

		return {"Source_id":Source_id,"Time":Time,"Memory":Memory,"Status":"AC","All_compare_out":{Test_case_name:"AC"},"All_stander_out":{Test_case_name:Stander_out}}	


if __name__ == "__main__" :
	while(1):
		# source_url="http://127.0.0.1:8000"
		source_url = "http://localhost:5000/dispatcher"
		requirement = requests.get(source_url)
		if requirement.status_code == 400:
			time.sleep(5)
			continue
		req_json = json.loads(requirement.text)

		keep = {}

		Submission_count = int(req_json['Submission_Count'])

		if Submission_count == 0 :
			time.sleep(5)
			continue

		result = {"Return_count":Submission_count,"Return_Set":{}}
		running_case = []
		for i in range (0,Submission_count):

			Mode = int(req_json["Submission_Set"][i]["Mode"])

			Problem_id = -1
			if Mode != 3:
				Problem_id = req_json["Submission_Set"][i]["Problem_id"]

			Source_id = req_json["Submission_Set"][i]["Source_id"]

			Keep = req_json["Submission_Set"][i]["Keep"]
			keep.update({"%s"%(Source_id):Keep})

			Test_case_count = int(req_json["Submission_Set"][i]["Test_case_count"])

			Time_limit = req_json["Submission_Set"][i]["Time_limit"]

			Memory_limit = req_json["Submission_Set"][i]["Memory_limit"]

			Language = req_json["Submission_Set"][i]["Language"]

			subprocess.run(["mkdir %s/Submission/%s"%(file_root,Source_id)],shell=True)

			Code = req_json["Submission_Set"][i]["Code"]

			lan = "";
			if Language == "c" :
				lan = "c"
			elif Language == "c++" :
				lan = "cpp"
			elif Language == "python" :
				lan = "exe"

			test = utility.write_file("%s/Submission/%s/%s.%s"%(file_root,Source_id,Source_id,lan),Code)
			if test == "Write_File_Error" :
				result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":"Write_File_Error","Compile_error_out":"","Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})
				continue

			# More Language
			try :
				if Language == "c++" :
					if utility.check_file_exist("%s/Submission/%s/%s.cpp"%(file_root,Source_id,Source_id)) == "Check_File_Exit_Error" :
						result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":"System_Error","Compile_error_out":"","Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})
						continue
					subprocess.run(["g++ %s/Submission/%s/%s.cpp -o %s/Submission/%s/%s.exe 2>%s/Submission/%s/%s.compile"%(file_root,Source_id,Source_id,file_root,Source_id,Source_id,file_root,Source_id,Source_id)],shell=True)
				elif Language == "c" :
					if utility.check_file_exist("%s/Submission/%s/%s.c"%(file_root,Source_id,Source_id)) == "Error" :
						result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":"System_Error","Compile_error_out":"","Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})
						continue
					subprocess.run(["gcc %s/Submission/%s/%s.c -o %s/Submission/%s/%s.exe 2>%s/Submission/%s/%s.compile"%(file_root,Source_id,Source_id,file_root,Source_id,Source_id,file_root,Source_id,Source_id)],shell=True)
			except :
				result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":"Compile_Error","Compile_error_out":"","Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})
				continue

			Status = "AC"
			Compile_error_out=""
			if Language == "c" or Language == "c++":
				Status , Compile_error_out = utility.checking_compile_result("%s/Submission/%s/%s.compile"%(file_root,Source_id,Source_id))
				if Status == "Check_Compile_Error" and Language != "python":
					result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":"Check_Compile_Error","Compile_error_out":"","Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})
					continue

			result["Return_Set"].update({Source_id:{"Mode":Mode,"Status":Status,"Compile_error_out":Compile_error_out,"Time":"-1","Memory":"-1","All_stander_out":{},"All_compare_out":{}}})

			if Status == "CE" :
				continue

			if Mode == 1 :
				for j in range (0,Test_case_count):
					Test_case_name=req_json["Submission_Set"][i]["All_test_case_general_submission"][j]["Test_case_name"]
					Test_case_answer_name=req_json["Submission_Set"][i]["All_test_case_general_submission"][j]["Test_case_answer_name"]
					running_case.append({"Mode":Mode,"Problem_id":Problem_id,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Test_case_name":Test_case_name,"Test_case_answer_name":Test_case_answer_name})

			if Mode == 2 :
				Correct_source_code = req_json["Submission_Set"][i]["Correct_source_code"]
				Test_case_name = req_json["Submission_Set"][i]["Self_test_case"][0]["Test_case_name"]
				Test_case_data = req_json["Submission_Set"][i]["Self_test_case"][0]["Data"]
				Correct_answer_language = req_json["Submission_Set"][i]["Correct_answer_language"]
				test = utility.write_file("%s/Submission/%s/%s.in"%(file_root,Source_id,Test_case_name),Test_case_data)
				running_case.append({"Mode":Mode,"Problem_id":Problem_id,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Correct_answer_language":Correct_answer_language,"Correct_source_code":Correct_source_code,"Test_case_name":Test_case_name})
			
			if Mode == 3 :
				User_id = req_json["Submission_Set"][i]["User_id"]
				for j in range (0,Test_case_count):
					Test_case_name = req_json["Submission_Set"][i]["Self_test_case"][j]["Test_case_name"]
					Test_case_data = req_json["Submission_Set"][i]["Self_test_case"][j]["Data"]
					utility.write_file("%s/Submission/%s/%s.in"%(file_root,Source_id,Test_case_name),Test_case_data)
					running_case.append({"Mode":Mode,"Source_id":Source_id,"Time_limit":Time_limit,"Memory_limit":Memory_limit,"Language":Language,"Test_case_name":Test_case_name})
				if utility.check_file_exist("%s/Submission/%s/%s.exe"%(file_root,Source_id,Source_id)) == "OK" :
					subprocess.run(["cp %s/Submission/%s/%s.exe %s/buffer/%s/%s.ansexe"%(file_root,Source_id,Source_id,file_root,User_id,Source_id)],shell=True)
					subprocess.run(["cp %s/Submission/%s/%s.exe %s/Submission/%s/%s.ansexe"%(file_root,Source_id,Source_id,file_root,Source_id,Source_id)],shell=True)

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
					result["Return_Set"][Source_id][key].update(value)
				elif key == "All_compare_out" :
					result["Return_Set"][Source_id][key].update(value)
	    
		for key,value in result["Return_Set"].items() :
			subprocess.run(["rm -r %s/Submission/%s"%(file_root,key)],shell=True)

		result=utility.change_json(result)
		with open("%s/Submission/Result.json"%(file_root),"w") as f:
			json.dump(result,f,indent = 4)

		result = json.dumps(result,indent = 4)
		# return_url="127.0.0.1:8000"
		return_url = "http://localhost:5000/dispatcher"
		# print(result)
		headers = {'Content-Type':"application/json"}
		response = requests.post(return_url, headers=headers , data=result)
		if response.status_code == 400:
			time.sleep(5)
		# print(response.status_code)
