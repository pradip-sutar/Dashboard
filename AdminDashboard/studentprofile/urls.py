from django.urls import path
from studentprofile import views

urlpatterns = [
    path('',views.student_page,name='student_page'),
    path('msg/',views.stu_messenger,name='stu_messenger'),
    path('pro/',views.stu_project,name='stu_project'),
    path('ass/',views.stu_assignment,name='stu_assignment'),
    path('sem/',views.stu_seminar,name='stu_seminar'),
    path('test/',views.test,name='test'),
]