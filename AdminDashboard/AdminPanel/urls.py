from django.urls import path
from . import views


urlpatterns = [

    path('',views.Admin,name='home'),
    path('analytics/',views.analytics,name='analytics'),
    path('notification/',views.notification,name='notification')
]