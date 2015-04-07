from urllib2 import Request, urlopen, URLError

request = Request('http://isithackday.com/arrpi.php?text=i like to swim when it is warm')

print request
