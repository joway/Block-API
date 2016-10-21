import os

MAIL_DEBUG = True

ENV = {
    'DEBUG': 'True',
    'MAIL_APP_USER': 'jowaywong',
    'MAIL_APP_KEY': 'fwPcJDvCdgEHsuLt',
    'SOCIAL_AUTH_QQ_KEY': '101330350',
    'SOCIAL_AUTH_QQ_SECRET': '0a3f8378119af6a231048ded9ad04fe2',
    'SOCIAL_AUTH_GITHUB_KEY': '497500e1266c7f2a4a42',
    'SOCIAL_AUTH_GITHUB_SECRET': 'd2e0c20abd1bd1683b2dab2d05b4d509ba23ec3a',
    'SOCIAL_AUTH_CODING_KEY': '8e0d5740d89efac69550bd1d0f7bde0e',
    'SOCIAL_AUTH_CODING_SECRET': '742ca24eb199febb7d97f844587e712f40f5c69e',
    'SECRET_KEY': '+p$6nzend1smn!*etr7k$9*g#$nj!lw#=u2e@ga82sra#nral3',
    'MYSQL_HOST': 'qd.joway.wang',
    'MYSQL_USERNAME': 'root',
    'MYSQL_PASSWORD': 'aliyunisGOOD!',
    'MYSQL_INSTANCE_NAME': 'block',
    'MYSQL_PORT': '3306',
    'QINIU_ACCESS_KEY': '8TiyJ3_BDDE_CQUnuZLr-5LjLkrYuUKSxU8ZQbpG',
    'QINIU_SECRET_KEY': 'cOEcxrH75kjNVJWwyuUj1h_7EMVYX7xn3cyIu5AK'
}

for i in ENV.keys():
    os.environ[i] = ENV[i]
