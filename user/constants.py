from django.utils.translation import ugettext_lazy as _

MAX_MAIL_INTERVAL_SECONDS = 60
MAX_MAIL_VALID_SECONDS = 12 * 60 * 60

# ERROR INFO
INVALID_CREDENTIALS_ERROR = _('Unable to login with provided credentials.')
INACTIVE_ACCOUNT_ERROR = _('User account is disabled.')

ANONYMOUS_USER = {
    'email': 'guest@joway.wang',
    'username': '游客',
    'avatar': 'https://avatars2.githubusercontent.com/u/2729079?v=3&s=40',
    'is_staff': False,
    'id': 0
}
