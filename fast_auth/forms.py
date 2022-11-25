from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(), max_length=50, required=True
    )
    email = forms.EmailField(
        label='Email', widget=forms.CharField(), max_length=50, required=True
    )
    password = forms.CharField(
        label='Password', widget=forms.CharField(), max_length=50, required=True
    )
    confirm_password = forms.CharField(
        label='Confirm password', widget=forms.CharField(), max_length=50, required=True
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Email or username ', widget=forms.TextInput(), max_length=50, required=True
    )
    password = forms.CharField(
        label='Password', widget=forms.CharField(), max_length=50, required=True
    )