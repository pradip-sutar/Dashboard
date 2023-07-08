from django.urls import path
from . import views


urlpatterns = [

    path('',views.Admin,name='home'),
    path('analytics/',views.analytics,name='analytics'),
    path('notification/',views.notification,name='notification'),
    path('group/',views.create_group,name='creategroup'),
    path('form/',views.Applicant_details,name='Applicant_details'),
    path('seminar/',views.Seminar_report,name='seminar_report'),
    path('project/',views.Projects_report,name='projects_report'),
    path('assign/',views.Assignment,name='assignment'),
    path('docs/',views.Docs,name='docs'),
    path('test/',views.test,name='test'),
    path('student_page/',views.student_page,name='student_page'),
    path('msg/',views.stu_messenger,name='stu_messenger'),
    path('pro/',views.stu_project,name='stu_project'),
    path('ass/',views.stu_assignment,name='stu_assignment'),
    path('sem/',views.stu_seminar,name='stu_seminar'),
    path('test/',views.test,name='test'),
    path('login/',views.login,name='login'),
]