from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Employee
from django.http import request,response,Http404
from LMS.forms import EditProfile,LeaveReq
# Create your views here.

class EmployeeListView(ListView):
    queryset = Employee.objects.all()
    template_name = 'employees/employeeList.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(EmployeeListView,self).get_context_data(*args,**kwargs)
        print(context['user'],'am here')
        return context


class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/employee.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(EmployeeDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        print(context)
        return context

class HodDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/employeehod.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(HodDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        print(context)
        return context


class DirectorDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/director.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(DirectorDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        print(context)
        return context


class AdminDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/employeeadmin.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(AdminDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        print(context)
        return context
