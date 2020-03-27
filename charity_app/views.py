from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Avg, Min
from django.contrib.auth import login, logout, authenticate
from charity_app.forms import *
from .models import *
from django.contrib.auth.models import User


from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta
#from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.exceptions import ObjectDoesNotExist
#from django.core.mail import EmailMessage
from django import forms
#from django.core.exceptions import ValidationError
#from django.core.validators import EmailValidator, URLValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class LandingPage(View):
    def get(self, request):
        quantity_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        organization_supported = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']
        foundations = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        return render(request, 'index.html', {"quantity_bags": quantity_bags,
                                              "organization_supported": organization_supported,
                                              "foundations": foundations,
                                              "organizations": organizations,
                                              "local_collections": local_collections})


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
        return render(request, 'register.html', {'form': form})


class UserPage(View):
    def get(self, request):
        logged_user = request.user.get_username()
        user_data = User.objects.get(username=logged_user)
        user_id = user_data.id
        user_donations = Donation.objects.filter(user=user_id)
        return render(request, 'user_page.html', {'user_data': user_data,
                                                  'user_donations': user_donations})
