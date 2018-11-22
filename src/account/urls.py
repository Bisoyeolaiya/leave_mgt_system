from django.contrib import admin
from django.conf.urls import url
from LMS.views import home
from . import views

urlpatterns = [
    url(r'^lms/home/', home),
    url(r'^signup/', views.SignUp,name='signup'),
    url(r'^login/', views.Login,name='login'),
    url(r'^logout/', views.Logout,name='logout'),

]