from django.db import models

# Create your models here.
from user.models import User
from .constants import ALINK_VERIFY_CODE_LENGTH, GRAPH_VERIFY_CODE_LENGTH
from .helper import link_captcha_expire_at, gen_link_captcha, gen_graph_captcha


class BaseCaptcha(models.Model):
    user = models.ForeignKey(User, null=True)

    class Meta:
        abstract = True


class LinkCaptcha(BaseCaptcha):
    expired_at = models.DateTimeField('过期时间', default=link_captcha_expire_at)
    captcha = models.CharField('链接验证码', max_length=ALINK_VERIFY_CODE_LENGTH,
                               blank=True, null=True, default=gen_link_captcha)


class GraphCaptcha(BaseCaptcha):
    captcha = models.CharField('图形验证码', max_length=GRAPH_VERIFY_CODE_LENGTH,
                               blank=True, null=True, default=gen_graph_captcha)
