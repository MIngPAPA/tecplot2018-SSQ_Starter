import os

os.system(r'tasklist | find /i  "rlm.exe" >pid.txt')
with open('pid.txt','r') as f:
	data=f.readlines()
if not data: #IF data=[] is true
	os.popen(r'YOUR AMEND PATH\rlm.exe') 
os.remove('pid.txt')
os.popen(r'YOUR TECPLOT PATH\tec360.exe')
