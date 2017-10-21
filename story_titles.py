from urllib2 import urlopen
from json import load

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'npr_api', 'r')
API_KEY = f.read().rstrip()
f.close()

url = 'http://api.npr.org/query?apiKey='
url = url + API_KEY
url += '&numResults=3&format=json&id=1001'
#url += raw_input("Which NPR ID do you want to query?")

response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
	print story['title']['$text']