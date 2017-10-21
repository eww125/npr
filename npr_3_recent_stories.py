from urllib2 import urlopen
from json import load

url = 'http://api.npr.org/query?apiKey='
key = 'MDAxNzgzOTYyMDEyMTUwMDkyMDM1ZWUwYw001'
url = url + key
url += '&numResults=3&format=json&id=1001'
#url += raw_input("Which NPR ID do you want to query?")
print url

response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
	print story['title']['$text']

#MDAxNzgzOTYyMDEyMTUwMDkyMDM1ZWUwYw001