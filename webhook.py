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


@app.route('/api/webhook/pull')
@auth.login_required
def run_pull():
    var = "Test"

    os.system("./test.sh")
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


if __name__ == '__main__':
    app.run(debug=True)
