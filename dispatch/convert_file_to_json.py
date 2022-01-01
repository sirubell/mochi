import os

def convert_file_to_json(file_place):
	f = open(file_place,"r")
	res = []
	Lines = f.readlines()
	for line in Lines:
		res.append(line)
	return res


res=convert_file_to_json("/home/piggy/Final/convert.c")
print(res)