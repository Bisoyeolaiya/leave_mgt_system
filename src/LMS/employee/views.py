from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import ListView,DetailView

from .models import Employee
=======
from django.http import request,response
>>>>>>> fe21d5f824e89fd690a0f9dd1af341643fd00b76
# Create your views here.

class EmployeeListView(ListView):
    queryset = Employee.objects.all()
    template_name = 'employees/employeeList.html'

    def get_context_data(self,*args,**kwargs):
        context = super(EmployeeListView,self).get_context_data(*args,**kwargs)
        return context


class EmployeeDetailView(DetailView):
    queryset = Employee.objects.all()
    template_name = 'employees/employeeList.html'

    def get_context_data(self,*args,**kwargs):
        context = super(EmployeeDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = EmployeeDetailView.objects.filter(pk)
        print(instance)
        return instance
