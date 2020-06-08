import os
import urllib.request
from json import load, dumps

f = open('credentials.yaml', 'r')
apiKey = f.read().rstrip()
f.close()

url = 'http://api.npr.org/query?apiKey='
url = url + apiKey 
url += '&numResults=3&format=json&id=1007'  # 1007 is science

wp = urllib.request.urlopen(url)
json_obj = load(wp)
pw = wp.read()
print(pw)

# JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

for story in json_obj['list']['story']:
    print("TITLE: " + story['title']['$text'] + "\n")
    print(story['byline'])
