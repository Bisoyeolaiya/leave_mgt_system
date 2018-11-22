from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from django.views import generic
from django.http import request,HttpResponseRedirect
from LMS.employee.models import Employee
from .models import CustomUser

from .forms import LoginForm,LmsSignUp,LMSRegForm

def SignUp(request):
    formdata = (request.POST or None)
    context={
        'form':formdata
    }
    
    if formdata is not None:
        staff_id = formdata.get('staff_id')
        f_name = formdata.get('f_name')
        l_name = formdata.get('l_name')
        dept_unit = formdata.get('dept_unit')
        home_addr = formdata.get('home_addr')
        designation = formdata.get('designation')
        phone_num = formdata.get('phone_num')
        email_addr = formdata.get('email_add')
        sex = formdata.get('sex')
        password = formdata.get('password')
        password1 = formdata.get('password1')
        userdata = (password,password1,f_name,l_name,sex,dept_unit,home_addr,designation,phone_num,email_addr)
        
        if ((staff_id[0:3]=='sta' ) and (password == password1)):
            user = CustomUser.object.create_staffuser(staff_id=staff_id,first_name=f_name,last_name=l_name,sex=sex,department_unit=dept_unit,home_address=home_addr,designation=designation,email_addr=email_addr,password=password)
            
            emp = Employee(user=user,staff_id=staff_id,f_name=f_name,l_name=l_name,sex=sex,dept_unit=dept_unit,home_addr=home_addr,designation=designation,email_addr=email_addr)

            emp.save()
            return redirect('/users/login/')

        elif ((staff_id[0:3]=='dir') and (password == password1)):
    
            user = CustomUser.object.create_director(staff_id=staff_id,first_name=f_name,last_name=l_name,sex=sex,department_unit=dept_unit,home_address=home_addr,designation=designation,email_addr=email_addr,password=password)
            
            emp = Employee(user=user,staff_id=staff_id,f_name=f_name,l_name=l_name,sex=sex,dept_unit=dept_unit,home_addr=home_addr,designation=designation,email_addr=email_addr)

            emp.save()
            return redirect('/users/login/')

        elif ((staff_id[0:3]=='hod') and (password == password1)):
    
            user = CustomUser.object.create_hod(staff_id=staff_id,first_name=f_name,last_name=l_name,sex=sex,department_unit=dept_unit,home_address=home_addr,designation=designation,email_addr=email_addr,password=password)
            
            emp = Employee(user=user,staff_id=staff_id,f_name=f_name,l_name=l_name,sex=sex,dept_unit=dept_unit,home_addr=home_addr,designation=designation,email_addr=email_addr)

            emp.save()
            return redirect('/users/login/')

        elif ((staff_id[0:3]=='adm') and (password == password1)):
    
            user = CustomUser.object.create_superuser(staff_id=staff_id,first_name=f_name,last_name=l_name,sex=sex,department_unit=dept_unit,home_address=home_addr,designation=designation,email_addr=email_addr,password=password)
            
            emp = Employee(user=user,staff_id=staff_id,f_name=f_name,l_name=l_name,sex=sex,dept_unit=dept_unit,home_addr=home_addr,designation=designation,email_addr=email_addr)

            emp.save()
            return redirect('/users/login/')
        else:
            return redirect('/users/signup/')
            
    return render(request,'registration/signup.html',context)

def Login(request):
    next = 'registration/login.html'
    form = (request.POST or None)
    context = {
        'form': form,
    }
    if form is not None:
        staff_id = form.get('staff_id')
        password = form.get('password')
        user = authenticate(request,staff_id=staff_id, password=password)
       
        if user is not None:
            login(request,user)
            if staff_id[0:3]=='sta':
                emp_data = Employee.objects.get(staff_id = staff_id)
                userid = emp_data.id
                urlredirect = f'/employee/dashboard/{userid}'
                return redirect(urlredirect)
                
            elif staff_id[0:3]=='hod':
                emp_data = Employee.objects.get(staff_id = staff_id)
                userid = emp_data.id
                urlredirect = f'/employee/hod/dashboard/{userid}'
                return redirect(urlredirect)

            
            elif staff_id[0:3]=='adm':
                emp_data = Employee.objects.get(staff_id = staff_id)
                userid = emp_data.id
                urlredirect = f'/employee/admin/dashboard/{userid}'
                return redirect(urlredirect)
            
            elif staff_id[0:3]=='dir':
                emp_data = Employee.objects.get(staff_id = staff_id)
                userid = emp_data.id
                urlredirect = f'/employee/director/dashboard/{userid}'
                return redirect(urlredirect)
            else:
                return redirect('registration/login.html')


    return render(request, "registration/login.html", context)

def Logout(request):
    logout(request)
    return redirect('/')

