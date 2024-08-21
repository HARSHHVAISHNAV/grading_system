from django.urls import path
from django.contrib import admin
from result_app.views import index, create_marking_scheme, track_progress, generate_reports, feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create_marking_scheme/', create_marking_scheme, name='create_marking_scheme'),
    path('track_progress/', track_progress, name='track_progress'),
    path('generate_reports/', generate_reports, name='generate_reports'),
    path('feedback/', feedback, name='feedback'),
]
