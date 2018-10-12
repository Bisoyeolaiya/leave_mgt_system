from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request,'lms/home.html', {})

def login(request):
    return render(request,'lms/login.html')

