import os
import requests
import sys
import time

def get_file_name(URL):
	for i in range(len(URL)-1,-1,-1):
		if URL[i]=="/":
			return URL[i+1:]

def downloadbar(alreadLenth,totalLenth,speed):
	count=int(alreadLenth/totalLenth*40)
	print("\r",end="")
	print("{",end="")
	for i in range(1,count+1):
		print("█",end="")
	for i in range(count+1,41):
		print("　",end="")
	print("}",end="")
	print(speed,end="")
	print("KB/S         ",end="")#多加空格防止下一行没有吧上一行覆盖掉导致速度显示异常

def download(URL):
	already_download=0
	Need_flash_bar=0
	time_start=time.time()
	resource=requests.get(URL,stream=True)
	content_size = int(resource.headers['content-length'])
	chunk_size=102400
	print("文件总大小:"+str(content_size/1024/1024)+"MB")
	print("保存位置:"+os.getcwd()+"\\",end="\n")
	print("正在下载",end="\n")
	with open(os.getcwd()+"\\"+get_file_name(URL),"wb") as file:
		for chunk in resource.iter_content(chunk_size=chunk_size):
			time_end=time.perf_counter()
			file.write(chunk)
			already_download=already_download+chunk_size
			count=int(already_download/content_size*40)
			if Need_flash_bar!=count:
				downloadbar(already_download,content_size,round(chunk_size/(time_end-time_start)/1024,2))
			Need_flash_bar=count
			time_start=time.perf_counter()
	print("\n下载完成")
	return

def main():
	URL=sys.argv[1]
	download(URL)

if __name__=="__main__":
	main()