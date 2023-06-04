from django.shortcuts import render

# Create your views here.
def Studentform(request):
    return render(request,'studentform.html')

def Applicant_details(request):
    return render(request,'applicant_details.html')

def Seminar_report(request):
    return render(request,'seminar_report.html')

def Projects_report(request):
    return render(request,'project_report.html')