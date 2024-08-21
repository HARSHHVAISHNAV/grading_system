from django.contrib import admin
from .models import (
    Courses,
    Students,
    MarksTheory,
    MarksPrac,
    CaseStudy,
    Design,
    Innovation,
    Quiz,
    Ppt,
    Gd,
    Presentation
)

# Register each model with the admin site
admin.site.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Customize as needed
    search_fields = ('title', 'description')  # Add fields you want to search

admin.site.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')  # Customize as needed
    search_fields = ('name',)

admin.site.register(MarksTheory)
class MarksTheoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'marks')  # Customize as needed
    search_fields = ('student__name',)

admin.site.register(MarksPrac)
class MarksPracAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'marks')  # Customize as needed
    search_fields = ('student__name',)

admin.site.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')

admin.site.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')

admin.site.register(Innovation)
class InnovationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')

admin.site.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')

admin.site.register(Ppt)
class PptAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')

admin.site.register(Gd)
class GdAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'student')  # Customize as needed
    search_fields = ('topic', 'student__name')

admin.site.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student')  # Customize as needed
    search_fields = ('title', 'student__name')
