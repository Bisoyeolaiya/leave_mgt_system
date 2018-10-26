from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required



def home(request):
    user = (request.user)
    context = {
        'user':user
    }
    return render(request,'lms/home.html',context)


