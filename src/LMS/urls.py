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
'''from LMS.employee.views import EmployeeListView,EmployeeDetailView'

urlpatterns = [
    url(r'^employees/',EmployeeListView.as_view()),
    url(r'^employees/(?P<pk>\d+)/$',EmployeeDetailView.as_view()),
]'''

from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from .views import home


''' from LMS.account.views import UserForm '''

 

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('account.urls')),
    url(r'^employee/', include('LMS.employee.urls')),
    url(r'^/', home)
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
