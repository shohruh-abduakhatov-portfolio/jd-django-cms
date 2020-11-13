import jwt
from jwt import ExpiredSignatureError


options = {'require_exp': True, 'verify_exp': True}


def decode_token(token):
    try:
        decoded = jwt.decode(token, verify=False, options=options)
    except ExpiredSignatureError:
        return None
    return decoded
