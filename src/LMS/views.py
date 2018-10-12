from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.

def home(request):
    return HttpResponse(request,'lms/navbar.html')

