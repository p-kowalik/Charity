from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserDataUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    repeat_new_password = forms.CharField(widget=forms.PasswordInput)
    new_email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(max_length=254, label="Wprowadź nowy email")
