# importing urllib library
from urllib.request import urlopen
  
# importing json
import json

def c2_ip():
    # store the URL in url as 
    # parameter for urlopen
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json"
      
    # store the response of URL
    response = urlopen(url)
      
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # TODO : 
    # if data_json is empty use local cache of c2 servers
    c2List = []

    for i in data_json:
        c2List.append(i['ip_address'])
    return c2List