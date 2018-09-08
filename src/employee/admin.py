from django.contrib import admin
import inspect
from . import models

# Register your models here.

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)
