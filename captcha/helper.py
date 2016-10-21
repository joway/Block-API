# coding: utf-8
from django.utils import timezone

from captcha.constants import ALINK_VERIFY_CODE_LENGTH, GRAPH_VERIFY_CODE_LENGTH
from utils.utils import get_random_string


def link_captcha_expire_at():
    return (timezone.now() + timezone.timedelta(hours=24))


def gen_link_captcha():
    return get_random_string(ALINK_VERIFY_CODE_LENGTH)


def gen_graph_captcha():
    return get_random_string(GRAPH_VERIFY_CODE_LENGTH)
