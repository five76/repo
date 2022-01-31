import yaml
from pprint import pprint
import subprocess
import os
import sys
import time
#from /home/ubuntu/repo/repo/projects/python/testcpp/workingrepo import *
from workingrepo import *

gp = False

if len(sys.argv) == 2:
    if sys.argv[1] == '-gp':
        gp = True
        print(gp)
        #tt = input('Input for next step')

#with open(path + 'remove_ex_repo.yaml') as f:
#   dict_remove_ex_repo = yaml.safe_load(f)

#for k,v in dict_remove_ex_repo.items():
#    for ex in v:
#        remove_ex_repo(clients,k,ex)

git_log_all(clients,gp)

