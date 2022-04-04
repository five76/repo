import os
import subprocess
import re
import json
from pprint import pprint
import sys
from modules import *



def ass_perm(users,dict_argv={}):

	#users=['sis112','sis113']
	comm = "vim-cmd vmsvc/getallvms > getallvms"
	result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
	l=result.communicate()[0]
	#print(l)	
	#list_VM=l.split("\n")                                 
	li_ass={}	
	eu = extract_user(dict_argv)
	if (eu):
		users=eu
	else:
		users=[u[-3:len(u)] for u in users ]
	
	#next=input("next?")	 
	
	host=extract_host(dict_argv)
	
		
	print(host)	
	
	
	for u in users:
		#ext_vid_host(l,h,u):
		#if host:
		if (host):
			for h in host:
				regex = re.compile(r'(\d+) +'+h+'_'+u)
				match = regex.findall(l)
				li_ass[u]=match
				#print(match)
		else:
			 regex = re.compile(r'(\d+) +\S+_'+u)
			 match = regex.findall(l)
			 li_ass[u]=match
			 #print(match)
	
	pprint(li_ass)
	for k,v in li_ass.items():
	#	print(k,v)
		for i in v:
			comm="vim-cmd vimsvc/auth/entity_permission_add vim.VirtualMachine:"+i+" sis"+k+" false Admin true"		
			print(comm)
			result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
			l=result.communicate()[0]
		#os.system(comm)
		#if (argv[2]!=uu):
		#	break

def ext_vid_host(l='',h='',u=''):
	#li_ass={}
	regex = re.compile(r'(\d+) +\S+'+h+'_'+u)
	match = regex.findall(l)
	#match = regex.findall(l)
	
	#li_ass[u]=match
	#print(match)
	return match

def run_command(li_ass={}):
	for k,v in li_ass.items():
		print(k,v)
		for i in v:
			comm="vim-cmd vimsvc/auth/entity_permission_add vim.VirtualMachine:"+i+" "+k+" false Admin true"
		 	result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
		 	l=result.communicate()[0]	



if __name__=='__main__':
	with open('users.json') as f:
		templates=json.load(f)	
	
	for u in templates:
		uu=u[-3:len(u)]
		#print(uu)
	
	#ass_perm(templates,sys.argv)
	dict_argv=create_dict_argv(sys.argv)
	pprint(dict_argv)
	ass_perm(templates,dict_argv)
	
	#pprint(extract_user(dict_argv))
