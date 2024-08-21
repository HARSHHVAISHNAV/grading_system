from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


from django.db import models

class Courses(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    course_title = models.CharField(max_length=255)
    credits = models.IntegerField()
    total_marks = models.IntegerField()
    type = models.CharField(max_length=1, choices=[('P', 'Practical'), ('T', 'Theoretical')])

    class Meta:
        db_table = 'courses'

class Students(models.Model):
    prn = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    year = models.IntegerField()
    division = models.IntegerField()
    email = models.EmailField(max_length=254, blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    acad_year = models.IntegerField()

    class Meta:
        db_table = 'students'

class MarksTheory(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    mse_marks = models.IntegerField()
    cce_marks = models.IntegerField()
    ese_marks = models.IntegerField()

    class Meta:
        db_table = 'marks_theory'

class MarksPrac(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    ciap_marks = models.IntegerField()
    esep_marks = models.IntegerField()

    class Meta:
        db_table = 'marks_prac'

class CaseStudy(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    understanding_marks = models.IntegerField()
    analysis_application_marks = models.IntegerField()
    solution_recommendation_marks = models.IntegerField()
    organization_structure_marks = models.IntegerField()
    clarity_writing_quality_marks = models.IntegerField()
    references_citation_marks = models.IntegerField()

    class Meta:
        db_table = 'case_study'

class Design(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    empathy_problem_definition_marks = models.IntegerField()
    ideation_marks = models.IntegerField()
    prototyping_marks = models.IntegerField()
    testing_feedback_marks = models.IntegerField()
    reflection_iteration_marks = models.IntegerField()

    class Meta:
        db_table = 'design'

class Innovation(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    originality_marks = models.IntegerField()
    relevance_impact_marks = models.IntegerField()
    feasibility_marks = models.IntegerField()
    implementation_strategy_marks = models.IntegerField()
    creativity_problem_solving_marks = models.IntegerField()

    class Meta:
        db_table = 'innovation'

class Quiz(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    mcqs_marks = models.IntegerField()
    short_answer_marks = models.IntegerField()
    full_answer_marks = models.IntegerField()
    partial_answer_marks = models.IntegerField()

    class Meta:
        db_table = 'quiz'

class Ppt(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    content_marks = models.IntegerField()
    organization_marks = models.IntegerField()
    design_marks = models.IntegerField()
    delivery_marks = models.IntegerField()
    audience_engagement_marks = models.IntegerField()
    qa_handling_marks = models.IntegerField()

    class Meta:
        db_table = 'ppt'

class Gd(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    content_knowledge_marks = models.IntegerField()
    communication_skills_marks = models.IntegerField()
    participation_contribution_marks = models.IntegerField()
    collaboration_teamwork_marks = models.IntegerField()

    class Meta:
        db_table = 'gd'

class Presentation(models.Model):
    prn = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='prn')
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE, to_field='course_code')
    content_marks = models.IntegerField()
    organization_marks = models.IntegerField()
    presentation_skills_marks = models.IntegerField()
    visual_aids_marks = models.IntegerField()
    response_to_questions_marks = models.IntegerField()

    class Meta:
        db_table = 'presentation'