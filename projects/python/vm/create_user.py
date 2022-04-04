import os
#import yaml 
import json

def create_user(users):
	for u in users:
		p = "P@ssword"
		c = "P@ssw0rd"
		comm = "esxcli system account add -i=\""+u+"\" -p=\"P@ssw0rd\" -c=\"P@ssw0rd\""
 		#comm = "esxcli system account remove -i=\""+u+"\""
	
		#print(comm)
		os.system(comm)

if __name__=='__main__':
	with open('users.json') as f:
		templates = json.load(f)
	create_user(templates)

