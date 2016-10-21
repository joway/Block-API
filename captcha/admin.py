from django.contrib import admin

# Register your models here.
from captcha.models import LinkCaptcha, GraphCaptcha

admin.register(LinkCaptcha)
admin.register(GraphCaptcha)
