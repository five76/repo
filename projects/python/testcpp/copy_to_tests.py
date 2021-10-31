import yaml
from pprint import pprint
import subprocess
import os
import time
#from /home/ubuntu/repo/repo/projects/python/testcpp/workingrepo import *
from workingrepo import *

#with open(path + 'remove_ex_repo.yaml') as f:
#   dict_remove_ex_repo = yaml.safe_load(f)

#for k,v in dict_remove_ex_repo.items():
#    for ex in v:
#        remove_ex_repo(clients,k,ex)
copy_to_tests(clients)

