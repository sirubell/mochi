from flask import jsonify
import os

from backend.config import parentdir

def convert_file_to_json(file_place):
	# return os.path.abspath(os.path.dirname(__file__)),file_place
	with open(os.path.join(parentdir, file_place), mode="r",encoding="utf-8") as f:
		res = []
		Lines = f.readlines()
		for line in Lines:
			res.append(line)
		return res

def convert_file_to_testcase():
	ret = []
	another_path = 'C:/Users/a2320/Desktop/coding/mochi/backend/test_buffer/3/'
	for i in range(0,11):
		s = ""
		with open(another_path+str(i)+".in",mode="r",encoding="utf-8") as f:
			now = f.readline()
			while now:
				s += now
				now = f.readline()
		ret.append(s)
	return ret

def convert_file_to_code(language):
	another_path = 'C:/Users/a2320/Desktop/coding/mochi/backend/test_buffer/1/'
	with open(another_path+"code."+language,mode="r",encoding="utf-8") as f:
		s = f.read()
		return s
	return ""
