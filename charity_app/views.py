from django.views import View
from django.http import HttpResponse
#from charity_app.forms import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta
from .models import *
from django.db.models import Count, Min, Sum, Avg
#from django.contrib.auth.models import User
#from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic.edit import UpdateView
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.exceptions import ObjectDoesNotExist
#
#from django.core.mail import EmailMessage
#from django import forms
#from django.core.exceptions import ValidationError
#from django.core.validators import EmailValidator, URLValidator
#from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm


class LandingPage(View):
    def get(self, request):
        quantity_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        organization_supported = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']
        return render(request, 'index.html', {"quantity_bags": quantity_bags,
                                              "organization_supported": organization_supported})


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')



