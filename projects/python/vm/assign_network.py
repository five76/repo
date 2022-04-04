import os
import subprocess
import re
import json
import sys

from pprint import pprint

def assign_networks(users,networks,hosts,argv=[]):
	path = "/vmfs/volumes/5f562b8c-13db7edf-5061-3c4a92deb010/"
	
	if (dict_argv['h'] and argv['u']):
		host=dict_argv['h']
		host_attr=networks[host]
		us=[]
		uu=dict_argv['u']
		if '-' in uu:
			#next=input("next?")
			start=int(uu[0:3])
			end=int(uu[-3:len(uu)])
			print(start)
			print(end)
			us=[str(i)  for i in range(start,end+1)]
			print(us)
			#next=input("next?")
		else:
			us.append(uu)
		
		#if len(us):
		
		for uu in us:
			assign_network(path,uu,host,host_attr)
		
		#else:
		#	assign_network(path,uu,host,host_attr)
		
		sys.exit(0)
	
	if (dict_argv['h']):
		host=dict_argv['h']
		host_attr=networks[host]
		for u in users:
			 uu=u[-3:len(u)]
			 for k,v in networks.items():
			 	assign_network(path,uu,host,host_attr)
		sys.exit(0)
		

		
	for u in users:
		uu=u[-3:len(u)]
		for k,v in networks.items():
			assign_network(path,uu,k,v)

def create_dict_argv(argv=[]):
	#pass
	dict_argv={}
	dict_argv['script']=argv[0]
	if len(argv)==1:
		return dict_argv
	
	for i in range(1,len(argv),2):
		print(i,' ',argv[i],' ' ,argv[i+1])
		dict_argv[argv[i][1:]]=argv[i+1]
		
	return dict_argv
	
	

def assign_network(path,uu,k,v):
	#path = "/vmfs/volumes/5f562b8c-13db7edf-5061-3c4a92deb010/"
	#net = networks[netw]
	#pprint(net)	
	h=k+"_"+uu
	fil=h+".vmx"		
	path_host = path +h +"/"+fil
	print(fil)
	for kk,vv in v.items():
		for kkk,vvv in vv.items():
			 comm1="/bin/sed -i /"+kk+"."+ kkk +"/d " + path_host
			 print(comm1)
			 result =subprocess.Popen(comm1.split(),stdout=subprocess.PIPE)
			 l=result.communicate()[0]
			 comm1="/bin/sed -i /"+kk+".startConnected/d " + path_host
			 result =subprocess.Popen(comm1.split(),stdout=subprocess.PIPE)
			 l=result.communicate()[0]
			 
			 for val in vvv:
			 	if kkk=="networkName":
			 		val=uu+"_"+val
			 	param=kk+"."+kkk+"=\""+val+"\""
			 	with open(path_host,'a') as f:
			 		f.write('\n'+param)
		
		
		
		
		
if __name__=='__main__':
	print(len(sys.argv))
	print('List argum')
	print(sys.argv)
	with open('assign_network.json') as f:
		networks=json.load(f)
			
	with open('users.json') as f:
		users=json.load(f)
	
	with open('hosts.json') as f1:
		hosts=json.load(f1)	
	
	dict_argv=create_dict_argv(sys.argv)
	pprint(dict_argv)
	
	#print(networks)
	#f sys.argv[1]=='-n':
	assign_networks(users,networks,hosts,dict_argv)
	#else:
	#print("No arg")
	#assign_networks(users,networks,hosts)
