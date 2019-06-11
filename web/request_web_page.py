from socket import gethostbyname
host = gethostbyname('www.baidu.com')   # Get the IP address from DNS.
print(host)

from urllib.request import urlopen
response = urlopen('http://www.baidu.com').read()    # request HTML context from a web url.
print(response[:15])
