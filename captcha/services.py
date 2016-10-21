import datetime

from django.utils import timezone

from captcha.exceptions import LinkCaptchaError, LinkCaptchaExpired, VerifyTimeFrequently
from captcha.models import LinkCaptcha
from user.constants import MAX_MAIL_INTERVAL_SECONDS


class CaptchaService(object):
    @classmethod
    def create_link_captcha(cls, user):
        link_captcha = LinkCaptcha.objects.get_or_create(user=user)[0]
        if (timezone.now() - link_captcha.expired_at) > datetime.timedelta(seconds=MAX_MAIL_INTERVAL_SECONDS):
            raise VerifyTimeFrequently
        return link_captcha

    @classmethod
    def check_link_captcha(cls, link_captcha):
        try:
            link_captcha = LinkCaptcha.objects.get(captcha=link_captcha)
        except LinkCaptcha.DoesNotExist:
            raise LinkCaptchaError
        if timezone.now() > link_captcha.expired_at:
            raise LinkCaptchaExpired
        user = link_captcha.user
        link_captcha.delete()
        return user
