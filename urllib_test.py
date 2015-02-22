import urllib.request
map = "maps"
response = urllib.request.urlopen("http://google.com/"+map)
html = response.read()
