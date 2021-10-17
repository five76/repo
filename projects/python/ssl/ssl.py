import yaml
from pprint import pprint
import subprocess

path ='/root/projects/python/ssl/'

with open(path + 'clients.yaml') as f:
    templates = yaml.safe_load(f)

with open(path + 'opensslcommand.yaml') as f:
    templates1 = yaml.safe_load(f)

with open(path + 'serial') as f:
    for i in f:
        YYY = i
#print(YYY)

pprint(templates)
ser=int(YYY)

for cl in templates:
    x = cl
    
    #print(x)
    #pprint(templates1)

    #YY = x[-2:]
    #pprint(YYY)
    #ser=int(YYY)
    result = []
    for i in templates1:
        s=i.replace('XXX',x)
        s=s.replace('YYY',str(ser))
        result.append(s)

    print(result)

    for i in result[:-2]:
        r = subprocess.run(i.split())
        #print(i.split())

    with open(path + 'clientVPN.yaml') as f:
        clientvpn = yaml.safe_load(f)

    with open('/etc/CA/clients/'+x+'/clientVPN.ovpn','w') as f:
        for i in clientvpn:
            s=i.replace('XXX',x)
            f.write(s+'\n')

    for i in result[-2:]:
        r = subprocess.run(i.split())
    
    with open('/etc/pki/CA/crlnumber','a') as f:
        f.write(str(ser)+'\n')    

    ser+=1

with open(path + 'serial','w') as f:
    f.write(str(ser))
