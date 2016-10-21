# coding: utf-8
from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class SignInForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
