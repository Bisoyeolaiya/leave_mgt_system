from django.contrib import admin
import inspect
from .models import Leave_req,Leave_type

admin.site.unregister(Leave_req)

# Register your models here.
'''for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)'''
