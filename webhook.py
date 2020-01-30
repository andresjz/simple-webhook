#!/usr/bin/env python
import os
import subprocess
import logging

from flask import Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config['WEBHOOK_SECRET_KEY'] = os.getenv('WEBHOOK_SECRET_KEY', 'The_Secret_key')
# app.logger = logging.getLogger()
#app.logger.setLevel(logging.ERROR)
auth = HTTPBasicAuth()

@app.route('/api/webhook/test', methods=['GET'])
@auth.login_required
def run_pull():
    var = "Test"
    # os.system("./test.sh &")
    subprocess.Popen(["nohup", "/bin/bash", "test.sh"])

    return jsonify({'data': 'Hello pulling, %s!' % var})


@app.before_request # Filter 1
def limit_remote_addr():
    print("Before the IP is: ", request.remote_addr)
    # if request.remote_addr != '10.20.30.40':
    #    abort(403)  # Forbidden

@auth.verify_password # Filter 2
def verify_password(username_or_token, password):
    s = Serializer(app.config['WEBHOOK_SECRET_KEY'])
    print("HOLA")
    print(s)
    try:
        data = s.loads(username_or_token)
        print(data)
        #logging.info("data {} ".format(data))
    except SignatureExpired:
        return False    # valid token, but expired
    except BadSignature:
        return False    # invalid token
    if not data:
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True,
    port=int(os.getenv('WEBHOOK_PORT', 8888)))

'''
https://stackoverflow.com/questions/89228/calling-an-external-command-from-python#2251026
https://stackoverflow.com/questions/2602052/how-to-call-a-program-from-python-without-waiting-for-it-to-return
https://stackoverflow.com/questions/49123439/python-how-to-run-process-in-detached-mode

https://www.fullstackpython.com/webhooks.html
'''