from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    midterm = models.DecimalField(max_digits=5, decimal_places=2)
    final = models.DecimalField(max_digits=5, decimal_places=2)
    continuous_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    practical = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"
    
class Subject(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    room = models.CharField(max_length=10)

class Student(models.Model):
    prn = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    div = models.CharField(max_length=5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)