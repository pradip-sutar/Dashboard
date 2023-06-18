from django.shortcuts import render

# Create your views here.
def student_page(request):
    return render(request,'studentprofile.html')

def stu_messenger(request):
    return render(request,'messenger.html')

def stu_assignment(request):
    return render(request,'stu_assignment.html')

def stu_seminar(request):
    return render(request,'stu_seminar_report.html')

def stu_project(request):
    return render(request,'stu_project_report.html')

def test(request):
    return render(request,'test.html')
