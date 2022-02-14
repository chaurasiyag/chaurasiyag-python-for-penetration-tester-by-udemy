import sys
import requests
import socket
import json
if len(sys.argv)<2:
	print('Usage:'+sys.argv[0]+'<link>{https or https included}')
	print("Don't include www in your link")
	sys.exit(1)

url=str(sys.argv[1])

arg=sys.argv[1]
if 'https://' in arg:
	gethostby_=socket.gethostbyname(sys.argv[1][8:])
else:
	gethostby_=socket.gethostbyname(sys.argv[1][7:])
print('\nThe IP address of '+sys.argv[1]+'is:' + gethostby_+'\n')


req_2=requests.get('https://ipinfo.io/'+gethostby_+'/json')
resp_=json.loads(req_2.text)

for i in resp_:
	print(i,resp_[i])



print('--------------------------')
print("Don't include www in your link\n otherwise you will get wrong answer or error")
print('--------------------------')