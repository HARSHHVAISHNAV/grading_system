from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Grade, Course
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def add_grade(request):
    if request.method == 'POST':
        course_id = request.POST['course']
        midterm = request.POST['midterm']
        final = request.POST['final']
        ca = request.POST['continuous_assessment']
        practical = request.POST['practical']
        student_id = request.POST['student']
        course = Course.objects.get(id=course_id)
        student = User.objects.get(id=student_id)
        grade = Grade(student=student, course=course, midterm=midterm, final=final, continuous_assessment=ca, practical=practical)
        grade.save()
        return redirect('home')
    courses = Course.objects.all()
    return render(request, 'add_grade.html', {'courses': courses})

def view_grades(request):
    grades = Grade.objects.all()
    return render(request, 'view_grades.html', {'grades': grades})

def home(request):
    return render(request, 'home.html')