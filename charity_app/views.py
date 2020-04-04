from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Avg, Min
from django.contrib.auth import login, logout, authenticate
from charity_app.forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.core.serializers import serialize
import json

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta
#from django.contrib.auth.mixins import PermissionRequiredMixin

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


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {"categories": categories,
                                             "institutions": institutions,
                                             })

    def post(self, request):
        bags_count = request.POST.get("bags")
        organization_id = request.POST.get("organization")
        organization_object = Institution.objects.get(id=organization_id)
        address = request.POST.get("address")
        phone_number = request.POST.get("phone")
        city = request.POST.get("city")
        zip_code = request.POST.get("postcode")
        pick_up_date = request.POST.get("data")
        pick_up_time = request.POST.get("time")
        pick_up_comment = request.POST.get("more_info")
        username = request.user.get_username()
        user_obj = User.objects.get(username=username)
        user_id = user_obj.id

        Donation.objects.create(quantity=int(bags_count),
                                institution=Institution.objects.get(id=organization_id),
                                address=address,
                                phone_number=phone_number,
                                city=city,
                                zip_code=zip_code,
                                pick_up_date=pick_up_date,
                                pick_up_time=pick_up_time,
                                pick_up_comment=pick_up_comment,
                                user=User.objects.get(id=user_id))
        return redirect('/confirmation/')


class ConfirmationView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'form-confirmation.html')


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


class UserDataUpdateView(View):
    def get(self, request):
        form = UserDataUpdateForm()
        return render(request, 'user_data_update.html', {'form': form})
