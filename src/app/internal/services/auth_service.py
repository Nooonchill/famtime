import hashlib
import hmac
import uuid
from datetime import datetime

import jwt
from pytz import timezone

from app.internal.models.app_user import AppUser
from app.internal.models.issued_token import IssuedToken
from app.internal.services.user_service import try_get_user_by_param
from config.settings import JWT_ISS, JWT_SECRET


def add_cookie(response, key, value):
    response.set_cookie(key=key, value=value, max_age=86400)
    return response

"""def generate_access_token(id: int):
    data = dict(
        iss=JWT_ISS,
        id=id,
        type='access',
        jti=str(uuid.uuid4()),
        iat=datetime.now(),
        nbf=datetime.now()
    )
    token = jwt.encode(data, JWT_SECRET, algorithm="HS256")
    return token


def generate_refresh_token(id: int):
    data = dict(
        iss=JWT_ISS,
        id=id,
        type='refresh',
        jti=str(uuid.uuid4()),
        iat=datetime.now(),
        nbf=datetime.now()
    )
    token = jwt.encode(data, JWT_SECRET, algorithm="HS256")
    IssuedToken.objects.create(
        jti=data['jti'],
        user= try_get_user_by_param('id', id),
        device_id=uuid.uuid4()
    )
    return token


def add_tokens_cookie(response, id):
    access_token = generate_access_token(id)
    refresh_token = generate_refresh_token(id)
    response.set_cookie(key='access_token', value=access_token, max_age=86400)
    response.set_cookie(key='refresh_token', value=refresh_token, max_age=2592000)
    return response


async def check_password(user, password):
    hash_input = hashlib.sha256(password.encode()).digest()
    hashed_password = str(hmac.new(hash_input, digestmod=hashlib.sha256).hexdigest())
    if hashed_password == user.password:
        return True
    return False"""
