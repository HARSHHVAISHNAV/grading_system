from django.shortcuts import render, get_object_or_404
from .models import Courses, Students, MarksTheory, MarksPrac, CaseStudy, Design, Innovation, Quiz, Ppt, Gd, Presentation

def index(request):
    return render(request, 'index.html')


def create_marking_scheme(request):
    prac_marks = MarksPrac.objects.all()
    return render(request, 'create_marking_scheme.html', {'prac_marks': prac_marks})

def track_progress(request):
    prac_marks = MarksPrac.objects.all()
    return render(request, 'track_progress.html', {'prac_marks': prac_marks})

def generate_reports(request):
    prac_marks = MarksPrac.objects.all()
    return render(request, 'generate_reports.html', {'prac_marks': prac_marks})

def feedback(request):
    prac_marks = MarksPrac.objects.all()
    return render(request, 'feedback.html', {'prac_marks': prac_marks})
