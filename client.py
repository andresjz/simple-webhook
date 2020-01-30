

import os
import httplib, urllib
import base64
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

SECRET_KEY  = os.getenv('WEBHOOK_SECRET_KEY', 'The_Secret_key')
WEBHOOK_URL = "127.0.0.1:"+os.getenv('WEBHOOK_PORT', '8888')

# expiration in sec
def generate_auth_token(user, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'id': user})


# export TOKEN=$(python client.py) remove runTestWeebhook function
# curl -u $TOKEN:unused -i -X GET http://127.0.0.1:8888/api/webhook/test
def runTestWeebhook(token):
    headers = {}
    headers['Authorization'] = "Basic %s" % base64.standard_b64encode(token + ":unused")

    h = httplib.HTTPConnection(WEBHOOK_URL)
    h.request( "GET", "/api/webhook/test", '', headers)
    response = h.getresponse()
    print (response.read())

if __name__ == '__main__':
    token = generate_auth_token('gitUser')
    runTestWeebhook(token)
    print(token)





