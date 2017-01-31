import requests
r = requests.post("http://127.0.0.1:8000/reports/sign_now/", files={'report' : open('test_new.txt', "r")})
status_code =  r.status_code
if(status_code != 200):
	print "Failed to sign!"
	exit(1)	
# Add some extra check on message
message = r.text

f = open("test_new.gpg", "w")
f.write(message)
f.close()

r =  requests.post("http://127.0.0.1:8000/reports/verify/", files={'report' : open('test_new.gpg', "r")})
print r.text
# Add some check on message
if(status_code != 200):
	print "Failed to verify!"
	exit(1)

