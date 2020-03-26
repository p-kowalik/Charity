from django.views import View
from django.http import HttpResponse
#from charity_app.forms import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta
from .models import *
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth.models import User
#from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.exceptions import ObjectDoesNotExist
#
#from django.core.mail import EmailMessage
from django import forms
#from django.core.exceptions import ValidationError
#from django.core.validators import EmailValidator, URLValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate
from charity_app.forms import *


class LandingPage(View):
    def get(self, request):
        quantity_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        organization_supported = Donation.objects.aggregate(Count('institution', distinct=True))['institution__count']
        foundations = Institution.objects.filter(type=1)
        for foundation in foundations:
            categories_allowed = Institution.categories
            print("categories_allowed: ", categories_allowed)

        organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        return render(request, 'index.html', {"quantity_bags": quantity_bags,
                                              "organization_supported": organization_supported,
                                              "foundations": foundations,
                                              "organizations": organizations,
                                              "local_collections": local_collections,
                                              "categories_allowed": categories_allowed})


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



# add user
#class AddUserView(LoginRequiredMixin, PermissionRequiredMixin, View):
#    login_url = '/login/'
#    permission_required = 'view_user'
#
#    def get(self, request):
#        form = AddUserForm()
#        return render(request, 'add_user_form.html', {'form': form})
#
#    def post(self, request):
#        form = AddUserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/main_menu/')
#        return render(request, 'add_user_form.html', {'form': form})
#
#
#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
#            return redirect('home')
#    else:
#        form = SignUpForm()
#    return render(request, 'signup.html', {'form': form})