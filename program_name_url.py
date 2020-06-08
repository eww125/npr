import os
import urllib.request
from urllib2 import urlopen
from json import load, dumps

f = open('credentials.yaml', 'r')
apiKey = f.read().rstrip()
f.close()

url = 'http://api.npr.org/query?apiKey='
url += apiKey
url += '&numResults=6&format=json&id=1149'  # 1007 is science
url += input("Which NPR ID do you want to query? ")

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

for story in json_obj['list']['story']:
    if ("show" in story):
        print("TITLE: " + story['title']['$text'])
        print("PROGRAM: " + story['show'][0]['program']['$text'])
        print("URL: " + story['link'][0]['$text'])
        #print "IMAGE: " + story['image'][0]['src'] + "\n"
        #print "IMAGE CAPTION: " + story['image'][0]['caption']['$text'] + "\n"
        #print "IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n"
        #print "MP3 AUDIO: "+ story['audio'][0]['format']['mp3'][0]['$text'] + "\n"
