import os
import time
def time_to_sec(t):
	second=int(t[0:t.index(':')])*3600+int(t[t.index(':')+1:])*60
	return second

def main():
	os.system("title 代强的定时关机程序")
	os.system("color 9e")
	shut_time=input("输入关机时间或者是距离关机多少秒:\n")
	if ':'in shut_time:
		second=time_to_sec(shut_time)-time_to_sec(time.strftime("%H:%M", time.localtime()))
		powerdown_time=shut_time
		if second>=0:
			os.system("shutdown -s -t "+str(second))
		else:
			second=second+12*3600
			os.system("shutdown -s -t "+str(second))
	else:
		os.system("shutdown -s -t "+shut_time)
		powerdown_time=str(int(time.strftime("%H", time.localtime()))+int(int(shut_time)/3600))+':'+str(int(time.strftime("%M", time.localtime()))+int(int(shut_time)%3600/60))

	print("系统将于%s关机,取消请输入n"%powerdown_time)
	if input()=='n':
		os.system("shutdown -a")
		
if __name__ == '__main__':
    main()