"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD
from LMS.employee.views import EmployeeListView,EmployeeDetailView

urlpatterns = [
    url(r'^employees/',EmployeeListView.as_view()),
    url(r'^employees/(?P<pk>\d+)/$',EmployeeDetailView.as_view()),
=======
from django.conf import settings
from .views import home
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',home),
>>>>>>> fe21d5f824e89fd690a0f9dd1af341643fd00b76
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
