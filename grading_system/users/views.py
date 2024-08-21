from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Grade, Course
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Subject, Student


def home_view(request):
    return render(request, 'home.html')

# def mysub_view(request):
#     return render(request, 'mysub.html') 

def login_view(request):
    return render(request, 'login.html')

def subject_detail(request, subject_id):
    # Handle the logic to display the subject details
    return render(request, 'subject_detail.html', {'subject_id': subject_id})
def mysub_view(request):
    subjects = [
        {'id': 1, 'name': 'Mathematics', 'code': 'MATH101', 'room': '301'},
        {'id': 2, 'name': 'Science', 'code': 'SCI101', 'room': '302'},
        {'id': 3, 'name': 'History', 'code': 'HIST101', 'room': '303'},
        {'id': 4, 'name': 'English', 'code': 'ENG101', 'room': '304'}
    ]
    context = {
        'subjects': subjects,
    }
    return render(request, 'mysub.html', context)