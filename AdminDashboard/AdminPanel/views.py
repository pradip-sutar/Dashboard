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

