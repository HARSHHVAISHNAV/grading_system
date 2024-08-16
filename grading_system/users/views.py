from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Grade, Course
from django.contrib.auth.models import User


def home_view(request):
    return render(request, 'home.html')

def mysub_view(request):
    return render(request, 'mysub.html') 

def login_view(request):
    return render(request, 'login.html')