from django.contrib import admin
from django.conf.urls import url
from LMS.views import home
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^lms/home/', home),
    url(r'^signup/', views.SignUp,name='signup'),
    url(r'^login/', views.Login,name='login'),
    url(r'^logout/', views.Logout,name='logout'),
=======
    
    url(r'^lms/home/', home,name='home'),
    url(r'^signup', views.SignUp.as_view(),name='signup'),
    url(r'^login', views.Login,name='login'),
    url(r'^logout', views.Logout,name='logout')
>>>>>>> bafa7ec6b3b2c4fbda5055dd72cb2fc4f0eb74b4

]