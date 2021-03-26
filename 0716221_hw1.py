import os
import sys
import threading
import asyncio
import hashlib
import requests
from bs4 import BeautifulSoup
import time

now = lambda: time.time()

def job1(onedata):		
	for ch5 in onedata:
		clist=[]
		for i in range(33,127):
			clist.append(chr(i))
		success=False
		for a in clist:
			for b in clist:
				for c in clist:
					for d in clist:
						for e in clist:
							s=hashlib.sha256()
							ch10=a+b+c+d+e+ch5
							s.update(ch10.encode("ascii"))
							h=s.hexdigest()
							if h[0:5]=='00000':
								print(a+b+c+d+e+ch5)
								success=True
								break
					if success:
						break
				if success:
					break
			if success:
				break	
					
	


def job2(onedata):
	for url in onedata:
		r=requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		print(soup.title.text)
			
	

def multiprocess1(balancedata,num):
	for onedata in balancedata:
		pid = os.fork()
		if pid == 0:
			for ch5 in onedata:
				clist=[]
				for i in range(33,127):
					clist.append(chr(i))
				success=False
				for a in clist:
					for b in clist:
						for c in clist:
							for d in clist:
								for e in clist:
									s=hashlib.sha256()
									ch10=a+b+c+d+e+ch5
									s.update(ch10.encode("ascii"))
									h=s.hexdigest()
									if h[0:5]=='00000':
										print(a+b+c+d+e+ch5)
										success=True
										break
							if success:
								break
						if success:
							break
					if success:
						break
			sys.exit(0)	
			
	if pid:
		for i in range(num):
			status = os.wait()


def multiprocess2(balancedata,num):
	for onedata in balancedata:
		pid = os.fork()
		if pid == 0:
			for url in onedata:
				r=requests.get(url)
				soup = BeautifulSoup(r.text, 'lxml')
				print(soup.title.text)
			sys.exit(0)	
			
	if pid:
		for i in range(num):
			status = os.wait() 
			
			
async def routine1(onedata):		
	for ch5 in onedata:
		clist=[]
		for i in range(33,127):
			clist.append(chr(i))
		success=False
		for a in clist:
			for b in clist:
				for c in clist:
					for d in clist:
						for e in clist:
							s=hashlib.sha256()
							ch10=a+b+c+d+e+ch5
							s.update(ch10.encode("ascii"))
							h=s.hexdigest()
							if h[0:5]=='00000':
								print(a+b+c+d+e+ch5)
								success=True
								break
					if success:
						break
				if success:
					break
			if success:
				break	
			
			
loop = asyncio.get_event_loop()	
async def routine2(onedata):		
	for url in onedata:
		#r=requests.get(url)
		r= await loop.run_in_executor(None, requests.get, url)
		soup = BeautifulSoup(r.text, 'lxml')
		print(soup.title.text)		
			
			
async def coroutine1():
	tasks = [routine1(i) for i in balancedata]
	results = await asyncio.gather(*tasks)
	#print(results)


'''
async def coroutine2():
	tasks = [routine2(i) for i in data]
	results = await asyncio.gather(*tasks)
	#print(results)
'''


#task1:Proof of Work; task2:catch title from URL
task = input()
#1:multithread; 2:multiprocess; 3:coroutine
secondline = input()
form = secondline.split()
#task number
t = input()
times = int(t)

data=[]
#multithread
if int(form[0]) ==1:
	num = int(form[1])
	data.clear()
	for i in range(times):
		d=input()
		data.append(d)
		
	start = now()	
	#loadbalance	
	balancedata=[]
	if times > num:
		div, mod = divmod(times,num)
		end=div
		for i in range(num):
			temp=[]
			temp.clear()
			for i in range(end-div,end):
				temp.append(data[i])
			balancedata.append(temp)
			end+=div
		for i in range(mod):
			balancedata[i].append(data[end-div+i])
	else:
		for i in data:
			balancedata.append([i])
			num=times

	
	if int(task)==1:		
		threads=[]
		for i in range(num):
			threads.append(threading.Thread(target=job1,args=(balancedata[i],)))
			threads[i].start()					
		for i in range(num):
			threads[i].join()
			
		print('TIME: ', now() - start)
	elif int(task)==2:
		threads=[]
		for i in range(num):
			threads.append(threading.Thread(target=job2,args=(balancedata[i],)))
			threads[i].start()
				
		for i in range(num):
			threads[i].join()
			
		print('TIME: ', now() - start)
	else:
		print("No this task")
#multiprocess
elif int(form[0]) ==2:
	num = int(form[1])
	data.clear()
	for i in range(times):
		d=input()
		data.append(d)
		
	start = now()	
	#loadbalance	
	balancedata=[]
	if times > num:
		div, mod = divmod(times,num)
		end=div
		for i in range(num):
			temp=[]
			temp.clear()
			for i in range(end-div,end):
				temp.append(data[i])
			balancedata.append(temp)
			end+=div
		for i in range(mod):
			balancedata[i].append(data[end-div+i])
	else:
		for i in data:
			balancedata.append([i])
			num=times

			
	if int(task)==1:
		multiprocess1(balancedata,num)
		print('TIME: ', now() - start)
	elif int(task)==2:
		multiprocess2(balancedata,num)
		print('TIME: ', now() - start)
	else:
		print("No this task")

#coroutine
elif int(form[0]) ==3:
	#num = int(form[1])
	data.clear()
	for i in range(times):
		d=input()
		data.append(d)
		
	start = now()
	
	balancedata=[]
	for i in data:
		balancedata.append([i])
					
	if int(task)==1:
		asyncio.run(coroutine1())
		print('TIME: ', now() - start)
	elif int(task)==2:
		tasks=[]
		for i in balancedata:
			task=loop.create_task(routine2(i))
			tasks.append(task)	
		loop.run_until_complete(asyncio.wait(tasks))
		#asyncio.run(coroutine2())
		print('TIME: ', now() - start)
	else:
		print("No this task")

else:
	print("No this function")
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



