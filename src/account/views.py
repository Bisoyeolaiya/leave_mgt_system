from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from django.http import request,HttpResponseRedirect
from LMS.employee.models import Employee

from .forms import CustomUserCreationForm,UserLoginForm,LmsSignUp

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    employee_form = LmsSignUp
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'



    def get_context_data(self,*args,**kwargs):
        employee_form = self.get_form(self.employee_form)
        context = {'employee_form':employee_form}
        return super(SignUp,self).get_context_data(**context)

    def post(self,request,*args,**kwargs):
        emp_form = LmsSignUp(request.POST or None)
        userform = CustomUserCreationForm(request.POST or None)
        if userform.is_valid():
            user = userform.save(commit=False)
            print(user)
            user.save()
            new_user = authenticate(username=user.username,password=user.password)
            login(request,new_user)
            emp_form.save()
            return HttpResponseRedirect(self.success_url)
        print(userform.error_messages)
        return HttpResponseRedirect('registration/signup')

def Login(request):
    
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/employee/dashboard/1.html')

    context = {
        'form': form,
    }
    return render(request, "registration/login.html", context)

def Logout(request):
    print('hello')
    return render(request, "registration/login.html",{})