from urllib2 import urlopen
website = urlopen("http://placekitten.com/")
kittens = website.read()
print kittens[559:1000]
