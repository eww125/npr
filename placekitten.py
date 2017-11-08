from urllib2 import urlopen
website = urlopen("http://placekitten.com")
#website = urlopen("https://raw.githubusercontent.com/eww125/ascii_art/master/eeyore")
kittens = website.read()
print kittens[0:1200]
