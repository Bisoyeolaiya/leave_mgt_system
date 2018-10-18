from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^dashboard/(?P<pk>\d+)',views.EmployeeDetailView.as_view(),name='employeepage')
]