import os

def convert_file_to_json(file_place):
	# return os.path.abspath(os.path.dirname(__file__)),file_place
	BASE = "c:\\Users\\a2320\\Desktop\\coding\\mochi\\backend\\"
	with open(BASE+file_place,mode="r",encoding="utf-8") as f:
		res = []
		Lines = f.readlines()
		for line in Lines:
			res.append(line)
		return res