from django.contrib import admin
from django.conf.urls import url
from LMS.views import home
from .views import login_view, register_view, logout_view

urlpatterns = [
    url(r'^lms/home/', home),
    url(r'^account/login/', login_view),
    url(r'^admin/', admin.site.urls),
    url(r'^account/register/', register_view),
    url(r'^account/logout/', logout_view)
]