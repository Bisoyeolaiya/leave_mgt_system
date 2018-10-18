
from django import forms
from django.forms import ModelForm

from LMS.employee.models import Employee
from LMS.leavemgt.models import Leave_req

class EditProfile(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



class LeaveReq(ModelForm):
    class Meta:
        model = Leave_req
        fields = ('leavetype','start_date','end_date','comment','upload',)


