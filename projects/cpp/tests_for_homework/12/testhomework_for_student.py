import glob
import os
import sys
import subprocess
import time
from pprint import pprint
import re
import yaml

d = os.getcwd() + '/'
arg1 = sys.argv[1] 

def test_file (in_file,out_obj_file,out_result):
    r = create_temp_cpp(in_file)
    if r == 0:
        return 0
    time.sleep(1)
    comm  = f'g++ {in_file} -lgtest  -lpthread -o {out_obj_file}'
    r = subprocess.run(comm.split())
    time.sleep(2)
    fold,fname = os.path.split(out_obj_file)
    comm = f'{fold}/./{fname}'
    #print(comm)
   # qqq=input("sada")
    r = subprocess.run(comm.split(),stdout = subprocess.PIPE, encoding='utf-8')
    result = re.findall(r'\S+ + (PASSED|FAILED)+ +.*',r.stdout)[-1]
    print(result)
    print(f'{in_file} - {result}')
    return result

def create_temp_cpp(in_file):
    fold,fname = os.path.split(in_file)
    s_file = f'{fold}/task_{fname[5:]}'
    if not os.path.exists(s_file):
        return 0
    o_file = f'{fold}/tasktemp_{fname[5:]}'
    with open(s_file) as f1:
        with open(o_file, 'w') as f2:
            for i in f1:
                o_text = i.replace('main','main1')
                f2.write(o_text)
    #print(f'task_{fname[5:]}')
    #pass
    return 1

def push_result_all(results=[]):
    passed_files=[]
    failed_files=[]
    os.chdir(d)
    for k,v in results.items():
        git_file = k.replace('test','task')
        #print(git_file)
        
        if v == 'PASSED':
            with open(f'{git_file}','a') as f:
                f.write('//verified')
            #  print(f)
            #git_file = k.replace('test','task')
            comm  = f'git add {git_file}'

            #print(comm)
            r = subprocess.run(comm.split())
            ccc = f'Done {git_file}'
            comm  = f'git commit -m {ccc}'
            r = subprocess.run(comm.split(' ',2))
            #print(comm)
            comm  = f'git push origin main'
            #print(comm)
            r = subprocess.run(comm.split())
            passed_files.append(git_file)
        else:
            if v == 'FAILED':
                failed_files.append(git_file)
        #ttt=input('dasd')
    print('Successful verification and sent to github: ')
    for f in passed_files:
        print(f)

    print('Failed verification: ')
    for f in failed_files:
        print(f)
    
    print ('To view errors ')
    print('insert command ./test_xx_xx.out')


def push_result(results=[],key=''):
    passed_files=[]
    failed_files=[]
    os.chdir(d)
    git_file = key.replace('test','task')   
        
    if results[key] == 'PASSED':
        with open(f'{git_file}','a') as f:
            f.write('//verified')
        #  print(f)
        #git_file = k.replace('test','task')
        comm  = f'git add {git_file}'

        #print(comm)
        r = subprocess.run(comm.split())
        ccc = f'Done {git_file}'
        comm  = f'git commit -m {ccc}'
        r = subprocess.run(comm.split(' ',2))
        #print(comm)
        comm  = f'git push origin main'
        #print(comm)
        r = subprocess.run(comm.split())
        passed_files.append(git_file)
        print('Successful verification and sent to github: ')
        print(git_file)
    else:
        if results[key] == 'FAILED':
            print('Failed verification: ')
            print(git_file)

#----------MAIN-----------------

with open(f'{d}testresult.yaml') as f:
    results = yaml.safe_load(f) 
#pprint(results)

if (arg1 == '-a'):
    files = glob.glob(f'{d}test_*.cpp')
    for i in files:
        in_file = i
        out_obj_file = i[:-3] + 'out'
        out_result = i[:-3] + 'txt'
       
        r = test_file(in_file,out_obj_file,out_result)
        if not r:
            continue
        fold,fname = os.path.split(in_file)
        results[fname] = r

    push_result_all(results)


#with open('sw_templates.yaml', 'w') as f:
    #yaml.dump(to_yaml, f, default_flow_style=False)

else:
    in_file = d + arg1
    out_obj_file = d+arg1[:-3] + 'out'
    out_result = d+arg1[:-3] + 'txt'
    #qqq=input("sada")
    r = test_file(in_file,out_obj_file,out_result)
    if r:
        fold,fname = os.path.split(in_file)
        results[fname] = r
    
    push_result(results,fname)

#pprint(results)

time.sleep(1)
files = glob.glob(f'{d}tasktemp_*.cpp')
for i in files:
    os.remove(i)
with open(f'{d}testresult.yaml','w') as f:
    yaml.dump(results, f, default_flow_style=False)

#with open(f'{d}testresult.yaml') as f:
#    results = yaml.safe_load(f) 
#pprint(results)
'''
passed_files=[]
failed_files=[]
os.chdir(d)
for k,v in results.items():
    git_file = k.replace('test','task')
    #print(git_file)
    
    if v == 'PASSED':
        with open(f'{git_file}','a') as f:
            f.write('//verified')
          #  print(f)
        #git_file = k.replace('test','task')
        comm  = f'git add {git_file}'

        #print(comm)
        r = subprocess.run(comm.split())
        ccc = f'Done {git_file}'
        comm  = f'git commit -m {ccc}'
        r = subprocess.run(comm.split(' ',2))
        #print(comm)
        comm  = f'git push origin main'
        #print(comm)
        r = subprocess.run(comm.split())
        passed_files.append(git_file)
    else:
        if v == 'FAILED':
            failed_files.append(git_file)
    #ttt=input('dasd')
print('Successful verification and sent to github: ')
for f in passed_files:
    print(f)

print('Failed verification: ')
for f in failed_files:
    print(f)
'''
