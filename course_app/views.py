from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render 
from course_app.models import Course, ProjectReg, Student 

def home(request):
    return render(request, 'homepage.html')

def reg(request): 
    if request.method == "POST": 
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student=Student.objects.get(id=sid) 
        course=Course.objects.get(id=cid) 
        res=student.enrolment.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 

        student.enrolment.add(course) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
    else: 
        students=Student.objects.all() 
        courses=Course.objects.all() 
        return render(request,"reg.html",{"students":students, "courses":courses})

def course_search(request): 
    if request.method=="POST": 
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student in s: 
            if student.enrolment.filter(id=cid): 
                student_list.append(student) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>") 
        return render(request,"selected_students.html",{"student_list":student_list}) 
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search.html",{"courses":courses})  
    

def add_project(request):
    if request.method == "POST":
        form = ProjectReg(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "<h1>Record inserted successfully</h1>"})
        else:
            return JsonResponse({"message": "<h1>Record not inserted</h1>"})
    else:
        form = ProjectReg()
        return render(request, "add_project.html", {"form": form})

    
from django.views import generic 
class StudentListView(generic.ListView): 
    model=Student 
    template_name="student_list.html" 

class StudentDetailView(generic.DetailView): 
    model=Student 
    template_name="student_detail.html"

def regaj(request): 
    if request.method == "POST": 
        sid=request.POST.get("sname") 
        cid=request.POST.get("cname") 
        student=Student.objects.get(id=sid) 
        course=Course.objects.get(id=cid) 
        res=student.enrolment.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 
        student.enrolment.add(course) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
    else: 
        students=Student.objects.all() 
        courses=Course.objects.all() 
        return render(request,"regaj.html",{"students":students, "courses":courses}) 
    
def course_search_ajax(request): 
    if request.method=="POST": 
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student in s: 
            if student.enrolment.filter(id=cid): 
                student_list.append(student) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>") 
        return render(request,"selected_students.html",{"student_list":student_list}) 
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search_aj.html",{"courses":courses})