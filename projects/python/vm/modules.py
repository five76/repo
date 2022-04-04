import sys

def create_dict_argv(argv=[]):
        #pass
        dict_argv={}
        dict_argv['script']=argv[0]
        if len(argv)==1:
		return dict_argv
        for i in range(1,len(argv),2):
        	#print(i,' ',argv[i],' ' ,argv[i+1])
                dict_argv[argv[i][1:]]=argv[i+1]
        return dict_argv

def extract_user(dict_argv={}):
	us=[]
        try:
        	uu=dict_argv['u']
                if '-' in uu:
                	#next=input("next?")
                        start=int(uu[0:3])
                        end=int(uu[-3:len(uu)])
                        us=[str(i)  for i in range(start,end+1)]
                else:
                	us.append(uu)	
        	return us
        except:
        	return 0

def extract_host(dict_argv={}):
	host=['']
	try:
		h=dict_argv['h']
		host=h.split(',')
		return host
	except:
		return 0 
	
	        
	         	
