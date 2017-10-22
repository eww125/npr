from urllib2 import urlopen
from json import load, dumps

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'npr_api', 'r')
key = f.read().rstrip()
f.close()

# transcript API call URL
url = 'http://api.npr.org/transcript?apiKey=' + key
url += '&format=json&id=152248901'

response = urlopen(url)
j = load(response)

# print transcript paragraphs
for paragraph in j["paragraph"]:
    print paragraph["$text"] + "\n"

# uncomment 3 lines below to see JSON output to file
# f = open('output.json', 'w')
# f.write(dumps(j, indent=4))
# f.close()



