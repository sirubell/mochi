import os,time,subprocess

def checking_compile_result(Source_id) :
	try :
		if os.stat(Source_id).st_size != 0 :
			f = open(Source_id,"r")
			return "CE",f.read()
		else :
			return "AC",""
	except:
		return "Check_Compile_Error","Check_Compile_Error"

def check_Runtime_Error(file_place) :
	try :
		if os.stat(file_place).st_size != 0 :
			return "RE"
		else :
			return "OK"
	except :
		return "Check_Runtime_Error"

def check_TLE_MLE(file_place,Memory_limit) :
	try :
		f = open(file_place,"r")
		text = f.readlines()
		res = []
		for i in range(len(text)) :
			res.append(text[i])
		if len(res) == 1 :
			return "OK"
		else :
			memory_size = int(res[1])
			Memory_limit = Memory_limit * 1024
			Maximum = Memory_limit * 0.9
			if memory_size > Maximum :
				return "MLE"
			else :
				return "TLE"
	except :
		return "Check_TLE_MLE_Error"

def check_time(file_place) :
	try :
		f = open(file_place,"r")
		text = f.readlines()
		res = []
		for i in range(len(text)) :
			res.append(text[i])
		return int((res[1][-5:-2]))+int((res[1][-7:-6]))*1000
	except :
		return "Check_Time_Error"

def check_memory(file_place) :
	try :
		f = open(file_place,"r")
		text = f.readlines()
		return int(text[0])
	except :
		return "Check_Memeory_Error"

def check_spec_memory(file_place) :
	try :
		f = open(file_place,"r")
		text = f.readlines()
		return int(text[1])
	except :
		return "Check_Spec_Memory_Error"


def compare_func(user_file,answer_file) :
	try :
		f1 = open(user_file,"r")
		f2 = open(answer_file,"r")

		try : 
			data1 = f1.read()
			data2 = f2.read()

			words1 = data1.split()
			words2 = data2.split()
			f1.close()
			f2.close()
			if words1 != words2 :
				return "WA"
			return "AC"

		except UnicodeError :
			return "OE"
	except :
		return "Compare_Func_Error"


def get_stander_out(file_place) :
	try :
		try :
			with open(file_place) as f :
				content = f.read().replace("\n"," ")
				return content
		except UnicodeError :
			return "OE"
	except :
		return "Get_Stander_Out_Error"

def write_file(file_place,data):
	try :
		fp = open(file_place,"w+")
		for i in range(len(data)) :
			fp.write(data[i])
		return "AC"
	except :
		return "Write_File_Error"

def check_file_exist(file_place) :
	try :
		if os.path.isfile(file_place) :
			return "OK"
		else :
			return "Check_File_Exit_Error"
	except :
		return "Check_File_Exit_Error"

def change_json(data) :
	res={}
	cnt = data["Return_count"]
	res["Return_count"]=cnt
	data = data["Return_Set"]
	res["Return_Set"]=[]
	for key in data:
		smalldata={}
		smalldata["Source_id"]=key
		smalldata["Mode"]=data[key]["Mode"]
		smalldata["Status"]=data[key]["Status"]
		smalldata["Compile_error_out"]=data[key]["Compile_error_out"]
		smalldata["Time"]=str(data[key]["Time"])
		smalldata["Memory"]=str(data[key]["Memory"])
		smalldata["All_stander_out"]=data[key]["All_stander_out"]
		smalldata["All_compare_out"]=[]
		for key2 in data[key]["All_compare_out"]:
			smalldata["All_compare_out"].append({str(key2):data[key]["All_compare_out"][key2]})
		res["Return_Set"].append(smalldata)
	return res
