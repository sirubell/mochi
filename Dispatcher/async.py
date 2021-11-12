from multiprocessing import Process, Pool
import os,time,subprocess

def main_map(submission):
	test_case_name=submission["test_case"]
	stdout_name=submission["stdout"]
	stderr_name=submission["stderr"]
	#subprocess.run(['bash','-c'," { time ./main <test_case/1.txt 1>finish/stdout 2>finish/stderr ; } 2> finish/time.txt "])
	#subprocess.run(['bash','-c'," { time /usr/bin/time -f \"%M KB\" -o finish/memory.txt ./main <test_case/1.txt 1>finish/stdout 2>finish/stderr ; } 2> finish/time.txt && python3 compare.py stdout 1.txt 1>finish/compare1.txt"])


	subprocess.run(['bash','-c'," { time /usr/bin/time -f \"%%M KB\" -o finish/memory%s ./main <test_case/1.txt 1>finish/%s 2>finish/%s ; } 2> finish/time%s && python3 compare.py %s 1.txt 1>finish/compare%s"%(test_case_name,stdout_name,stderr_name,test_case_name,stdout_name,stdout_name)])
	#subprocess.run(["time docker run -i --rm -v /home/piggy/async:/home/piggy/async runner ./main <test_case/{test_case} 1>finish/{stdout} 2>finish/{stderr}".format(test_case=test_case_name,stdout=stdout_name,stderr=stderr_name)],shell=True)
	return "Finish"

if __name__ == "__main__" :

	subprocess.run(["g++ source/main.cpp -o main 1>finish/compile_stdout.log 2>finish/compile_stderr.log"],shell=True)
	inputs = []
	for i in range(1,100):
		inputs.append({"test_case":"1.txt","stdout":str(i)+".txt","stderr":str(i)+".txt"})
	pool=Pool()
	pool_outputs=pool.map(main_map,inputs)
	pool.close()
	pool.join()
	print(pool_outputs)
