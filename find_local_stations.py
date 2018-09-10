import urllib.request
from json import load

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'npr_api_key', 'r')
key = f.read().rstrip()
f.close()

def build_api_call(key):
    zip_code = input("Enter your zip code:")
    url = 'http://api.npr.org/stations?apiKey=' + key
    url += '&format=json'
    url += "&zip=" + zip_code
    return url


def call_station_api(url):
    response = urllib.request.urlopen(url)
    j = load(response)
    return j


def parse_station_json(json_obj):
    for station in json_obj['station']:
        print( station['callLetters']['$text'] + ": " +
                station['marketCity']['$text'] + ", " +
                station['state']['$text'])
        print("Frequency:", station['frequency']['$text'], station['band']['$text'])

        if 'url' in station:
            print("MP3 Streams: ")
            for link in station['url']:

                if link["type"] == "Audio MP3 Stream":
                    print("\t", link["title"], " - ", link["$text"])


url = build_api_call(key)
print("URL: ", url)
json_obj = call_station_api(url)
parse_station_json(json_obj)

