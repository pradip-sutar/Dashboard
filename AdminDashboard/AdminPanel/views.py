from django.shortcuts import render

# Create your views here.
def Admin(request):
    return render(request,'admindashboard.html')

def analytics(request):
    return render(request,'analytics.html')

def notification(request):
    return render(request,'notification.html')

def create_group(request):
    return render(request,'creategroup.html')

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

def Studentform(request):
    return render(request,'studentform.html')

def Applicant_details(request):
    return render(request,'applicant_details.html')

def Seminar_report(request):
    return render(request,'seminar_report.html')

def Projects_report(request):
    return render(request,'project_report.html')

def Assignment(request):
    return render(request,'Assignment.html')

def Docs(request):
    return render(request,'documents.html')

def test(request):
    return render(request,'test.html')

