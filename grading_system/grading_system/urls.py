"""
URL configuration for grading_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home_view, name='home'),
    path('login/', user_views.login_view, name='login'),
    path('mysub/', user_views.mysub_view, name='mysub'), 
    path('dashboard/', user_views.home_view, name='dashboard'), 
    path('subject/<int:subject_id>/', user_views.subject_detail, name='subject_detail'),
    path('students/', user_views.student_list, name='student_list'),
    path('students/add/', user_views.student_add, name='student_add'),
    path('students/edit/<str:pk>/', user_views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/delete/<str:pk>/', user_views.StudentDeleteView.as_view(), name='student_delete'),
    path('student/<str:pk>/grade/', user_views.grade_student, name='student_grade'),
    path('student/<str:pk>/detail/', user_views.student_detail, name='student_detail'),
    path('student-details/<int:student_id>/', user_views.student_details, name='student_details'),
    path('add-subject/', user_views.add_subject, name='add_subject'),
]
