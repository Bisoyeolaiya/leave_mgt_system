from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Employee
from django.http import request,response,Http404
from LMS.forms import EditProfile,LeaveReq
from django.views.generic.detail import SingleObjectMixin
# Create your views here.

class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/employee.html'
      

    def get_context_data(self,*args,**kwargs):
        context = super(EmployeeDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        return context
        
    def save(self, *args, **kwargs):
        print(request.POST)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        pk = self.kwargs['pk']
        emp = Employee.objects.get(user = self.request.user)
        staff_id = emp.staff_id
        print(staff_id,pk,emp.id)
        if ((staff_id[0:3] == 'sta') and (pk == str(emp.id))):
            return super(EmployeeDetailView, self).dispatch(*args, **kwargs)  
        else:
            return redirect('/')

    

class HodDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/hod.html'
  
    def get_context_data(self,*args,**kwargs):
        context = super(HodDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        return context

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        pk = self.kwargs['pk']
        emp = Employee.objects.get(user = self.request.user)
        staff_id = emp.staff_id
        print(staff_id,staff_id[0:2],type(pk),type(emp.id))
        if ((staff_id[0:3] == 'hod') and (pk == str(emp.id))):
            print('success')
            return super(HodDetailView, self).dispatch(*args, **kwargs)  
        else:
            return redirect('/')


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

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        pk = self.kwargs['pk']
        emp = Employee.objects.get(user = self.request.user)
        staff_id = emp.staff_id
        print(staff_id,pk,emp.id)
        if ((staff_id[0:3] == 'dir') and (pk == str(emp.id))):
            return super(DirectorDetailView, self).dispatch(*args, **kwargs)  
        else:
            return redirect('/')


class AdminDetailView(DetailView):
    queryset = Employee.objects.all()
    emp_form_class = EditProfile
    LeaveReq_form_class = LeaveReq
    template_name = 'dashboard/hrAdmin.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(AdminDetailView,self).get_context_data(*args,**kwargs)
        context['leave_req']=self.LeaveReq_form_class()
        context['EditProfile']=self.emp_form_class()
        print(context)
        return context

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        pk = self.kwargs['pk']
        emp = Employee.objects.get(user = self.request.user)
        staff_id = emp.staff_id
        print(staff_id,pk,emp.id)
        if ((staff_id[0:3] == 'adm') and (pk == str(emp.id))):
            return super(AdminDetailView, self).dispatch(*args, **kwargs)  
        else:
            return redirect('/')