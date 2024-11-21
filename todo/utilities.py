import jwt
from django.conf import settings


def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload  # Will return the decoded user data (like username, email)
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
