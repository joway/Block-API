from captcha.services import CaptchaService
from config.settings import DOMAIN_URL
from sendcloud.constants import SendCloudTemplates
from sendcloud.exceptions import SendcloudError
from sendcloud.utils import sendcloud_template
from utils.jwt import get_jwt_token
from .exceptions import UserNotExist, PasswordError, EmailExist, UserHasActivated
from .models import User


class UserService(object):
    @classmethod
    def login(cls, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotExist
        if user.check_password(password):
            return get_jwt_token(user)
        else:
            raise PasswordError

    @classmethod
    def register(cls, email, password):
        user, is_create = User.objects.get_or_create(email=email)
        if not is_create:
            raise EmailExist
        user.set_password(password)

        link_captcha = CaptchaService.create_link_captcha(user=user)

        if sendcloud_template(to=[email],
                              tpt_ivk_name=SendCloudTemplates.REGISTER,
                              sub_vars={'%username%': [email],
                                        '%url%': [DOMAIN_URL + '/user/activate?confirm=' + link_captcha.captcha]}):
            user.save()
            return user
        else:
            raise SendcloudError

    @classmethod
    def activate(cls, alink_verify_code):
        user = CaptchaService.check_link_captcha(alink_verify_code)
        if not user.is_active:
            raise UserHasActivated
        user.is_active = True
        user.save()
        return user

    @classmethod
    def disactivate(cls, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotExist
        if not user.is_active:
            return False
        user.is_active = False
        user.save()
        return True

    @classmethod
    def logout(cls):
        pass
