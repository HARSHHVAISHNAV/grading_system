from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Courses, Students, MarksTheory, MarksPrac, CaseStudy, Design, Innovation, Quiz, Ppt, Gd, Presentation
from django.views.generic.edit import UpdateView , DeleteView


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



# View to list all students
def student_list(request):
    students = Students.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add Student View
def student_add(request):
    if request.method == 'POST':
        # Get data from form
        prn = request.POST['prn']
        name = request.POST['name']
        branch = request.POST['branch']
        year = request.POST['year']
        division = request.POST['division']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        acad_year = request.POST['acad_year']

        # Create a new Student record
        Students.objects.create(prn=prn, name=name, branch=branch, year=year, division=division, email=email, mobile_number=mobile_number, acad_year=acad_year)
        return redirect('student_list')
    return render(request, 'student_add.html')

class StudentUpdateView(UpdateView):
    model = Students
    fields = ['name', 'branch', 'year', 'division', 'email', 'mobile_number', 'acad_year']
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'  # Ensures the context variable is 'student'

class StudentDeleteView(DeleteView):
    model = Students
    template_name = 'student_delete.html'
    context_object_name = 'student'  # Ensure this matches the name used in your template
    success_url = reverse_lazy('student_list')


def grade_student(request, pk):
    # Retrieve the student based on the primary key
    student = get_object_or_404(Students, pk=pk)
    
    # Redirect to the student detail page
    return redirect('student_detail', pk=student.pk)


def student_detail(request, pk):
    student = get_object_or_404(Students, pk=pk)
    return render(request, 'student_detail.html', {'student': student})


def student_details(request, student_id):
    try:
        student = Students.objects.get(pk=student_id)
        data = {
            'prn': student.prn,
            'name': student.name,
            'branch': student.branch,
            'year': student.year,
            'division': student.division,
            'email': student.email,
            'mobile_number': student.mobile_number
        }
        return JsonResponse(data)
    except Students.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    


def add_subject(request):
    if request.method == 'POST':
        # Process form data here
        pass
    return render(request, 'add_subj.html')