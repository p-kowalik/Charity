from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class DonationSummaryForm(forms.Form):
    quantity = forms.IntegerField()
    categories = forms.CharField()
    institution = forms.CharField()
    address = forms.Textarea()
    phone_number = forms.CharField(max_length=64)
    city = forms.CharField(max_length=64)
    zip_code = forms.CharField(max_length=64)
    pick_up_date = forms.DateField()
    pick_up_time = forms.TimeField()
    pick_up_comment = forms.Textarea()
    user = forms.IntegerField()


class UserDataUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.PasswordInput()
    repeat_new_password = forms.PasswordInput()
    new_email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
