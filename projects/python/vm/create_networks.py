import os
import subprocess
import re
import json
from pprint import pprint
def create_networks(users,networks):
	
	for u in users:
		uu=u[-3:len(u)]
		#Create Switch for user
		vs = "vSwitch"+uu
		comm1 = "esxcli network vswitch standard add --vswitch-name=" + vs
		
		result =subprocess.Popen(comm1.split(),stdout=subprocess.PIPE)
		l=result.communicate()[0]
		         
		#print(comm1)
		
		#Start Vlan 
		vl=10
		for n in networks:
			
			#Create PortGroup for network and set VLAN
			pg=uu+"_"+n
			comm2 = "esxcli network vswitch standard portgroup add --portgroup-name="+ pg +"  --vswitch-name="+vs
			comm3 = "esxcli network vswitch standard portgroup set -p "+ pg + " --vlan-id " + str(vl) 
			
			result1 =subprocess.Popen(comm2.split(),stdout=subprocess.PIPE)
			l=result1.communicate()[0]
			
			result2 =subprocess.Popen(comm3.split(),stdout=subprocess.PIPE)
			l=result2.communicate()[0]
			
			vl=vl+10 #insrease vlan

if __name__=='__main__':
	with open('networks.json') as f:
		networks=json.load(f)
			
	with open('users.json') as f:
		users=json.load(f)
	
	
	create_networks(users,networks)


