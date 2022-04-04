import os
import subprocess
import re
import json
from pprint import pprint
def create_networks(users,networks):
	
	#for u in users:
	
	#users=['sis112','sis113']
	#comm1 = "esxcli network vswitch standard add --vswitch-name=vSwitch112"
	#result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
	#l=result.communicate()[0]
	#print(l)	
	#list_VM=l.split("\n")                                 
	#li_ass={}	
	for u in users:
		uu=u[-3:len(u)]
		vs = "vSwitch"+uu
		#comm1 = "esxcli network vswitch standard add --vswitch-name=" + vs
		
		#result =subprocess.Popen(comm1.split(),stdout=subprocess.PIPE)
		#l=result.communicate()[0]
		         
		#print(comm1)
		vl=10
		for n in networks:
			pg=uu+"_"+n
			
			comm2 = "esxcli network vswitch standard portgroup remove --portgroup-name="+ pg +"  --vswitch-name="+vs
			#comm3 = "esxcli network vswitch standard portgroup set -p "+ pg + " --vlan-id " + str(vl) 
			
			result1 =subprocess.Popen(comm2.split(),stdout=subprocess.PIPE)
			l=result1.communicate()[0]
			
			#result2 =subprocess.Popen(comm3.split(),stdout=subprocess.PIPE)
			#l=result2.communicate()[0]
			
			#print(comm2)
			#print(comm3)
			vl=vl+10
		#regex = re.compile(r'(\d+) +\S+_'+uu)
		#match = regex.findall(l)
		#li_ass[u]=match
		comm1 = "esxcli network vswitch standart remove --vswitch-name=" + vs
		result =subprocess.Popen(comm1.split(),stdout=subprocess.PIPE)
		l=result.communicate()[0]
		                  
	#next=input("NEXT?")		
	#pprint(li_ass)
	#for k,v in li_ass.items():
	#	print(k,v)
	#	for i in v:
	#		comm="vim-cmd vimsvc/auth/entity_permission_add vim.VirtualMachine:"+i+" "+k+" false Admin true"		
	#		#print(comm)
	#		result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
	#		l=result.communicate()[0]
		#os.system(comm)

if __name__=='__main__':
	with open('networks.json') as f:
		networks=json.load(f)
			
	with open('users.json') as f:
		users=json.load(f)
	
	#for u in templates:
	#	#uu=u[-3:len(u)]
	#	print(u)
	
	#ass_perm(templates)
	create_networks(users,networks)
	#comm = "vim-cmd vmsvc/getallvms > getallvms"
	#result =subprocess.Popen(comm.split(),stdout=subprocess.PIPE)
	#l=result.communicate()[0]
	#result=subprocess.check_output(comm.split(),stderr=subprocess.STDOUT)
	#print(l) 	
	
	#list_VM=l.split("\n")

	#for ll in list_VM:
	#	print(ll)
	
	#regex = re.compile(r'(\d+) +\S+_'+uu)
	#match = regex.findall(l)
	#print(match)


