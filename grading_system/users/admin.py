from django.contrib import admin
from .models import Students, Courses, MarksTheory, MarksPrac, CaseStudy, Design, Innovation, Quiz, Ppt, Gd, Presentation

# Registering the models
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(MarksTheory)
admin.site.register(MarksPrac)
admin.site.register(CaseStudy)
admin.site.register(Design)
admin.site.register(Innovation)
admin.site.register(Quiz)
admin.site.register(Ppt)
admin.site.register(Gd)
admin.site.register(Presentation)
