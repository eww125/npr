from urllib2 import urlopen

# Add your code here!
website = urlopen("http://placekitten.com/")
kittens = website.read()
print kittens[559:1000]