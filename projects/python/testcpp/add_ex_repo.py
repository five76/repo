import yaml
from pprint import pprint
import subprocess
import os
import time
#from /home/ubuntu/repo/repo/projects/python/testcpp/workingrepo import *
from workingrepo import *

with open(path + 'clients.yaml') as f:
   clients = yaml.safe_load(f)
pprint (clients)
with open(path + 'add_ex_repo.yaml') as f:
   dict_add_ex_repo = yaml.safe_load(f)

for k,v in dict_add_ex_repo.items():
    #print(k)
    for ex in v:
        #print(ex)
        copy_ex_repo(clients,k,ex)

add_ex_repo(clients)


