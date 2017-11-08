
from urllib2 import urlopen
from json import load, dumps

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'npr_api', 'r')
API_KEY = f.read().rstrip()
f.close()

url = 'http://api.npr.org/query?apiKey='
key = API_KEY
url = url + key
url += '&numResults=6&format=json&id=1149'  # 1007 is science
url += raw_input("Which NPR ID do you want to query? ")

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

for story in json_obj['list']['story']:
    if ("show" in story):
        print "TITLE: " + story['title']['$text'] + "\n"
        print "PROGRAM: " + story['show'][0]['program']['$text'] + "\n"
        print "URL: " + story['link'][0]['$text'] + "\n"
        #print "IMAGE: " + story['image'][0]['src'] + "\n"
        #print "IMAGE CAPTION: " + story['image'][0]['caption']['$text'] + "\n"
        #print "IMAGE CREDIT: " + story['image'][0]['producer']['$text'] + "\n"
        #print "MP3 AUDIO: "+ story['audio'][0]['format']['mp3'][0]['$text'] + "\n"
