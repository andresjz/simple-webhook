

import os
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

SECRET_KEY = 'The_Secret_key'

# expiration in sec
def generate_auth_token(user, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'id': user})


if __name__ == '__main__':
    print('Generating random token...')
    token = generate_auth_token('covadongaUser')
    print('Token: %s' % token)
