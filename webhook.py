#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'The_Secret_key'
auth = HTTPBasicAuth()


@app.route('/api/webhook/test', methods=['GET'])
@auth.login_required
def run_pull():
    var = "Test"

    os.system("./test.sh &")
    return jsonify({'data': 'Hello pulling, %s!' % var})


@auth.verify_password
def verify_password(username_or_token, password):
    user = verify_auth_token(username_or_token)
    if not user:
        return False
    return True


def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False    # valid token, but expired
    except BadSignature:
        return False    # invalid token
    return data


@app.before_request
def limit_remote_addr():
    print("Before the IP is: ", request.remote_addr)
    # if request.remote_addr != '10.20.30.40':
    #    abort(403)  # Forbidden


if __name__ == '__main__':
    app.run(debug=True)

'''
https://stackoverflow.com/questions/89228/calling-an-external-command-from-python#2251026
https://stackoverflow.com/questions/2602052/how-to-call-a-program-from-python-without-waiting-for-it-to-return
https://stackoverflow.com/questions/49123439/python-how-to-run-process-in-detached-mode

https://www.fullstackpython.com/webhooks.html
'''