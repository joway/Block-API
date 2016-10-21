from django.utils import timezone

from oauth.constants import GrantTypes
from oauth.exceptions import ApplicationNotExist, GrantNotExist, ClientSecretError, RefreshTokenError, TokenNotExist, \
    TokenExpired, GrantTypeNotMatch
from oauth.generators import generate_access_token, generate_refresh_token
from oauth.models import Grant, Application, Token
from utils.jwt import get_jwt_token


class OauthService(object):
    @classmethod
    def grant(cls, client_id, user):
        try:
            app = Application.objects.get(client_id=client_id)
        except Application.DoesNotExist:
            raise ApplicationNotExist
        grant = Grant.objects.create_grant(app=app, user=user)
        return grant

    @classmethod
    def gen_tokens(cls, client_id, client_secret, code, grant_type, redirect_url=None, state=None):
        try:
            app = Application.objects.get(client_id=client_id)
            if app.client_secret != client_secret:
                raise ClientSecretError
        except Application.DoesNotExist:
            raise ApplicationNotExist
        try:
            grant = Grant.objects.get(code=code, application__client_id=client_id)
        except Grant.DoesNotExist:
            raise GrantNotExist
        if app.grant_type == GrantTypes.AUTHORIZATION_CODE:
            access_token = generate_access_token()
            refresh_token = generate_refresh_token()
        elif app.grant_type == GrantTypes.JWT_BEARER:
            access_token = get_jwt_token(user=grant.user)
            refresh_token = generate_refresh_token()
        else:
            raise GrantTypeNotMatch
        tokens = Token.objects.create_token(app=app, user=grant.user,
                                            access_token=access_token,
                                            refresh_token=refresh_token)
        return tokens

    @classmethod
    def refresh_token(cls, client_id, client_secret, refresh_token):
        try:
            grant = Grant.objects.get(application__client_id=client_id,
                                      application__client_secret=client_secret)
        except Grant.DoesNotExist:
            raise GrantNotExist
        try:
            tokens = Token.objects.get(application__client_id=client_id, user=grant.user)
            if tokens.refresh_token != refresh_token:
                raise RefreshTokenError
        except Token.DoesNotExist:
            raise TokenNotExist
        if grant.application.grant_type == GrantTypes.AUTHORIZATION_CODE:
            access_token = generate_access_token()
            refresh_token = generate_refresh_token()
        elif grant.application.grant_type == GrantTypes.JWT_BEARER:
            access_token = get_jwt_token(user=grant.user)
            refresh_token = generate_refresh_token()
        else:
            raise GrantTypeNotMatch
        tokens.access_token, tokens.refresh_token = access_token, refresh_token
        tokens.save()
        return tokens

    @classmethod
    def verify_access_token(cls, access_token):
        try:
            token = Token.objects.get(access_token=access_token)
            if cls.is_expired(token.expire_at):
                raise TokenExpired
        except Token.DoesNotExist:
            raise TokenNotExist
        return token

    @classmethod
    def verify_refresh_token(cls, refresh_token):
        try:
            token = Token.objects.get(refresh_token=refresh_token)
            if cls.is_expired(token.expire_at):
                raise TokenExpired
        except Token.DoesNotExist:
            raise TokenNotExist
        return token

    @classmethod
    def is_expired(cls, expire_at):
        if timezone.now() < expire_at:
            return False
        else:
            return True
