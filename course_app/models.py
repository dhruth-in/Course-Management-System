from django import forms
from django.db import models 
from django.forms import ModelForm 
# Create your models here. class 
class Meeting(models.Model): 
    meeting_code=models.CharField(max_length=100) 
    meeting_dt=models.DateField(auto_now_add=True)
    meeting_subject=models.CharField(max_length=100) 
    meeting_np=models.IntegerField() 

class Course(models.Model): 
    course_code=models.CharField(max_length=40) 
    course_name=models.CharField(max_length=100) 
    course_credits=models.IntegerField(blank=True, null=True) 
    def str (self): 
        return self.course_name 

class Student(models.Model): 
    student_usn = models.CharField(max_length=20) 
    student_name = models.CharField(max_length=100) 
    student_sem = models.IntegerField() 
    enrolment = models.ManyToManyField(Course) 

    def __str__(self): 
        return f"{self.student_name} ({self.student_usn})"
 

class Project(models.Model): 
    Student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    Topic=models.CharField(max_length=200) 
    Langauges=models.CharField(max_length=200) 
    Duration=models.IntegerField() 

class ProjectReg(ModelForm): 
    class Meta:
        model = Project
        fields = ['Student', 'Topic', 'Langauges', 'Duration']

    Student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        empty_label="Select Student"
    )