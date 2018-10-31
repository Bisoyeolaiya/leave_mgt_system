from django.contrib import admin
import inspect
from . import models

# Register your models here.

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        if (obj.__module__== "account.models"):
            continue
        admin.site.register(obj)
