from . import views
from django.conf.urls import url

urlpatterns = [
    
    url(r'^dashboard/(?P<pk>\d+)',views.EmployeeDetailView.as_view(),name='employeepage'),
    url(r'^dashboard/(?P<pk>\d+)/edit-profile',views.EmployeeDetailView.save,name='editpage'),



    url(r'^hod/dashboard/(?P<pk>\d+)',views.HodDetailView.as_view(),name='hodpage'),
    url(r'^director/dashboard/(?P<pk>\d+)',views.DirectorDetailView.as_view(),name='directorpage'),
    url(r'^admin/dashboard/(?P<pk>\d+)',views.AdminDetailView.as_view(),name='adminpage')
]