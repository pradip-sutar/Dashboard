from django.urls import path
from . import views

urlpatterns = [
    
    path('form/',views.Applicant_details,name='Applicant_details'),
    path('seminar/',views.Seminar_report,name='seminar_report'),
    path('project/',views.Projects_report,name='projects_report'),
    path('assign/',views.Assignment,name='assignment'),
    path('docs/',views.Docs,name='docs'),
]