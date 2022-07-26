import os 
dirName='tempDir'
from IP_Carve import ip_carve
from fetchAPI import c2_ip

def C2checker():
    res = []
    for path in os.listdir(dirName):
        address = os.path.join(dirName, path)
        if os.path.isfile(address):
            res+=ip_carve(address)

    c2List = c2_ip()
    vulnerableIP = list(set(res).intersection(c2List))
    if vulnerableIP.count!=0:
        print("Files contain vulnerable IP Addresses")
        print(vulnerableIP)
    else:
        print("File is safe to import")