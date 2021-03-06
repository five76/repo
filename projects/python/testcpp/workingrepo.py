import yaml
import threading
from pprint import pprint
import subprocess
import os
import time
import re
import glob
#import pymysql
import mysql.connector

path =os.getcwd()+'/'
path_update = '/home/ubuntu/oapisip/comp/'
path_copy = '/home/ubuntu/oapisip/comp/tests/'
path_source =  '/home/ubuntu/oapisip/comp/oap-is-20-template/exercises/'
num_chap = {'01':'01_alg','02':'02_langcpp','03':'03_linprogr','04':'04_if','05':'05_for','06':'06_while','07':'07_array','08':'array2','12':'12_funct'}
with open(path + 'clients.yaml') as f:
    clients = yaml.safe_load(f)


#==== functions =============================================
def delete_repo(clients=[]):
    for  cl in clients:
        comm = 'rm -fr ' + path_update+cl+'/.git'
        #time.sleep(1)
        r = subprocess.run(comm.split())
        time.sleep(1)
        comm = 'rm -fr ' + path_update+cl
        #time.sleep(1)
        r = subprocess.run(comm.split())
        time.sleep(2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
def clone_repo(clients=[]):
    for  cl   in clients:
        print( f'Clone repo for {cl}')
        chdir =  path_update
        os.chdir(chdir)
        comm = 'git clone git@github.com:five76/'+ cl+ '.git'
        #time.sleep(1)
        r = subprocess.run(comm.split())

        time.sleep(5)
    os.chdir(path)
    
        #omm = 'rm -fr ' + path_update+cl
        #time.sleep(1)
        #r = subprocess.run(comm.split())
        #time.sleep(2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def create_folders(clients=[],chapters=[],folders=[]):
    for cl in clients:
        for ch in chapters:
            i  = ch.replace('XXX',cl)
            for f in folders:
                ff = i+'/'+f
                comm = 'mkdir -p ' + ff
                print(comm)
                try:
                    r = subprocess.run(comm.split())
                    r1 = subprocess.run(['touch',ff + '/README.md'])
                   # a=[cl]
                   # git_update(a)
                except:
                    print (f'Folders {ff} exist')
        git_update(cl)
        time.sleep (5)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def git_update_all(clients=[]):
    for  cl in clients:
        chdir =  path_update + cl
        os.chdir(chdir)
        git_add = 'git add ' + ' .'
        git_commit = r'git commit -m "UpdatedPrepod"'
        git_push = 'git push origin main'
        r = subprocess.run(git_add.split())
        time.sleep(3)
        r1 = subprocess.run(git_commit.split())
        time.sleep(3)
        r2 = subprocess.run(git_push.split())
        time.sleep(3)
    os.chdir(path)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def git_pull_all_thread(cl=''):
    #for cl in clients:
    print(f'git pull for {cl}')
    chdir =  path_update  + cl
    os.chdir(chdir)
    git_pull = 'git pull'
    r = subprocess.run(git_pull.split())
    #time.sleep(5)
    #os.chdir(path)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def git_pull_all(clients=[]):
    threads = []
    for cl in clients:
        thread = threading.Thread(target=git_pull_all_thread, args=(cl,))
        thread.start()
        threads.append(thread)

        #print(f'git pull for {cl}')
        #chdir =  path_update  + cl
        #os.chdir(chdir)
        #git_pull = 'git pull'
        #r = subprocess.run(git_pull.split())
        #time.sleep(5)
    for thread in theads:
        thread.join()

    os.chdir(path)

#++++++++++++++++++++++++++++++++++++++++

def git_pull(cl=''):
    print(f'git pull for {cl}')
    chdir =  path_update  + cl
    os.chdir(chdir)
    git_pull = 'git pull'
    r = subprocess.run(git_pull.split())
    #time.sleep(5)
    os.chdir(path)

#+++++++++++++++++++++++++++++++++++++++++++



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def git_update(client):
    print(f'updating {client}')
    cl = client   
    chdir =  path_update + cl
    print (chdir)
    os.chdir(chdir)
    git_config = 'git config pull.rebase false'
    git_pull = 'git pull'
    git_add = 'git add ' + ' .'
    git_commit = r'git commit -m "UpdatedPrepod"'
    git_push = 'git push origin main'
    r00 = subprocess.run(git_config.split())
    r0 = subprocess.run(git_pull.split())
    r = subprocess.run(git_add.split())
    r1 = subprocess.run(git_commit.split())
    r2 = subprocess.run(git_push.split())
    os.chdir(path)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def git_log_all(clients=[],gp=False):
    """
    ?????????? ???? ???????????????????????? ?????????????????? ???????? ????????????  ???????????????? ??????????????, ?????????????? commit "Done task_xx.xx.cpp"
    ?????????? ???????????????????? ?? ???????? git_log_dir.yaml
    gp - ????????????????, ???????????????????????? ?????????????????????????? ?????????????????? ?????????????? git pull. ????-?????????????????? ???????? (False)
    """
    threads = []

    git_log_dir = {}
    if gp:
        for cl in clients:
            #git_pull(cl)
            thread = threading.Thread(target=git_pull_all_thread, args=(cl,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        
        
        
    for cl in clients:    
        print(f'git log for {cl}')
        chdir =   path_update  + cl
        os.chdir(chdir)
        #git_log = 'git log --grep=done --grep=task_'
        git_log = 'git log --grep=done --grep=task'

        #git_log = 'git log | egrep  -i \'done +task \'' 

        r = subprocess.run(git_log.split(),stdout=subprocess.PIPE, encoding='utf-8')
        match=re.findall(r'[Dd]one (task_\d+_\d+.cpp) *',r.stdout)
        #match=re.findall(r'[Dd]one (task[_ ]) *',r.stdout)
        ll = list(set(match))
        #print(ll)
        git_log_dir[cl]= ll
        #ss = r.stdout.split('\n')
        #for i in ss:
            #match=regex.findall(i)
         #   pprint (i)
        #pprint(r.stdout)
        #print (git_log)
        #time.sleep(2)
    os.chdir(path)     
    #pprint(git_log_dir)
    #to_yaml = {'trunk': trunk_template, 'access': access_template}

    with open('git_log_dir.yaml', 'w') as f:
             yaml.dump(git_log_dir, f, default_flow_style=False)

            #with open('sw_templates.yaml') as f:
            #       print(f.read())

#+++++++++++++++++++++++++++++++++++++++++++++++++++
def conndb(sql='',val=[],):
    con=mysql.connector.connect(host='localhost',
        user='admin',
        password='AbrecJcz123',
        database='oapisip')
        #charset='utf8')
        #ursorclass=pymysql.cursors.DictCursor)

    with con:

        cur = con.cursor()
        #sql = "INSERT INTO marks (studID,taskID,mark,date,attempt) VALUES (%s,%s,%s,%s,%s)"
        #val=  ('isip20_01','task_03_01',0,'2021-11-09',0)
        cur.executemany(sql,val)

        con.commit()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

def conndb_select(sql=''):
    con=mysql.connector.connect(host='localhost',
        user='admin',
        password='AbrecJcz123',
        database='oapisip')
        #charset='utf8')
        #ursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()
    cur.execute(sql)
    #cur.execute("SELECT studID,taskID FROM marks")

    myresult = cur.fetchall()
    #pprint(myresult)
    return myresult


#++++++++++++++++++++++++++++++++++++++++++++++++++++

def copy_to_tests(clients):
    """
    ?????????????????????? ???????????? ?????????????? (task_.xx_xx.cpp) ???? ?????????????????? .../home ?? ???????????????? ?????? ????????????????
    ?????????? ?????????????????????? ?? git_log_dir.yaml
    """
    print('copy_to_tests')
    
    with open(path + 'git_log_dir.yaml') as f:
        git_log_dir = yaml.safe_load(f)
    date = '2021-11-09'
    attempt = 0
    mark = -1
    val=[]
    sql = "SELECT studID,taskID FROM marks"
    exis_marks = conndb_select(sql)



    #for cl in clients:

        #print(cl)
    for k,v in git_log_dir.items():
        #print(k)
        #print(len(v))
        if len(v)  != 0:
            for i  in v:
                ch  = i[5:7]
                dd =  f'{path_copy}{k}/{ch}'
                #print(dd)
                #aaa=input('asdsa')
                if not(os.path.exists(dd)):
                    comm = f'mkdir -p {dd}'
                    #print(comm)
                    #aaa=input('sdsds')
                    r = subprocess.run(comm.split())
                
                #print(ch)
                #print(dd)
                #print(num_chap[ch])
                #print(i)
              
                comm = f'cp  /home/ubuntu/oapisip/comp/{k}/exercises/{num_chap[ch]}/home/{i} {path_copy}{k}/{ch}/{i}'
                #print(comm)
                #aaa=input('dwedwedw')
                try:
                    r  = subprocess.run(comm.split())
                except:
                    raise
                if r.returncode == 0:
                    taskID  = i[0:10]
                    #print(k,' - ',taskID,' - ',mark,' - ',date,' - ',attempt)
                    
                    if (k,taskID)  in exis_marks:
                        continue
                    
                    val. append((k,taskID,mark))
                    #aaa=input('dwedwedw')
                    #print(comm)               
    pprint(val)
    #aaa=input('insert into db')
    sql = "INSERT INTO marks (studID,taskID,mark) VALUES (%s,%s,%s)"
    
    conndb(sql,val)
 
#++++++++++++++++++++++++++++++++++++++++++++++++++

def copy_tests_to_clients(clients):
    """ 
    ?????????????????????? ???????????? ???????????? (test_xx_xx.cpp) ?? ???????????????? ?? ???????????????????????? ?????????????????? ??????????????????
    ???????? ?? ???????????? ???????????? ?????????????????????? ?? tests.yaml
    """
    print('copy_tests_to_client')
    
    with open(path + 'tests.yaml') as f:
        tests_dir = yaml.safe_load(f)
    for cl in clients:
         for k,v in tests_dir.items():
             dd =  f'{path_copy}{cl}/{k}'
             test_files=glob.glob(f'{v}/test*')
             if os.path.exists(dd):
                 for ff in test_files:
                     comm = f'cp {ff} {dd}'
                     r =  subprocess.run(comm.split())
#++++++++++++++++++++++++++++++++++++++++++++++++++


def add_ex_repo(clients=[], chap='', ex=''):
    print ('add _ex_repo')
    for cl in clients:
        #comm = 'cp '+ path_source + chap + ex + ' '+ path_update + cl +'/exercises/' + chap + ex
        #print(comm)
        #print (cl)
        #r = subprocess.run(comm.split())
        #time.sleep(10)
        git_update(cl)
        
    os.chdir(path) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def copy_ex_repo(clients=[], chap='', ex=''):
    print (f'coping {ex}')
    for cl in clients:
        comm = ' cp '+ path_source + chap + ex + ' '+ path_update + cl +'/exercises/' + chap + ex
        #print(comm)
        #print (cl)
        r = subprocess.run(comm.split())
        #time.sleep(10)
        #git_update(cl)
        
    os.chdir(path)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def remove_ex_repo(clients=[], chap='', ex=''):
    print('remove_ex_repo')
    for cl in clients:
        comm = 'rm -fr '+ path_update + cl +'/exercises/' + chap + ex
        r = subprocess.run(comm.split())
        git_update(cl)
        
    os.chdir(path)


def msql():
    """
    ???????????????????? ?????????????? marks ???????? ???????????? ?????????????????????? ?????????????? (task_.xx_xx.cpp)
    ?????????? ?????????????????????? ?? git_log_dir.yaml
    """
    print('msql')

    with open(path + 'git_log_dir.yaml') as f:
        git_log_dir = yaml.safe_load(f)
    '''
    con=mysql.connector.connect(host='localhost',
        user='admin',
        password='AbrecJcz123',
        database='oapisip')
        #charset='utf8')
        #ursorclass=pymysql.cursors.DictCursor)

    with con: 
 
        cur = con.cursor()
        sql = "INSERT INTO marks (studID,taskID,mark,date,attempt) VALUES (%s,%s,%s,%s,%s)"
        val=  ('isip20_01','task_03_01',0,'2021-11-09',0)
        cur.execute(sql,val)
        con.commit()

    '''
    date = '2021-11-09'
    attempt = 0
    mark = 2
    val = []
    for cl in clients:
        #print(cl)
        for k,v in git_log_dir.items():
            if cl != k:
                continue
            #print(k)
            #print(len(v))
            if len(v)  != 0:
                for i  in v:
                    taskID  = i[0:10]
                    #print(cl,' - ',taskID,' - ',mark,' - ',date,' - ',attempt)
                    val.append((cl,taskID,mark,date,attempt))
    #pprint(val)
    sql = "INSERT INTO marks (studID,taskID,mark,date,attempt) VALUES (%s,%s,%s,%s,%s)"
    conndb(sql,val)
#============================================================
     

if __name__ == '__main__':
    #    pass
    with open(path + 'clients.yaml') as f:
        clients = yaml.safe_load(f)
    #pprint (clients)
    #clients=['isip20_02','isip20_03']

    with open(path + 'chapters.yaml') as f:
        chapters = yaml.safe_load(f)
    #pprint (chapters)

    folders = ['class','home']

    #clone_repo(clients)

    #---------------------------------------------------------
    # Create folders 
    create_folders(clients, chapters,folders)

    #-----------------------------------------------------

    #git_update(clients)
