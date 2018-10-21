from django.contrib import admin
from django.conf.urls import url
from LMS.views import home
from . import views

urlpatterns = [
    url(r'^lms/home/', home),
    url(r'^signup/', views.SignUp.as_view(),name='signup'),
    url(r'^login/', views.Login,name='login'),
    

]