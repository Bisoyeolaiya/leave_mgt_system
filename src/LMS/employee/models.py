from django.db import models
from LMS.leavemgt.models import Leave_req
import uuid
from account.models import CustomUser
from django.urls import reverse


# Create your models here.
class Approved(models.Model):
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    dept_name = models.ForeignKey('Dept', on_delete=models.CASCADE)
    hod_comment = models.TextField(verbose_name='hod comment')
    hr_comment = models.TextField(verbose_name='hr comment')
    hod_approved = models.BooleanField(default=False)
    hr_approved = models.BooleanField(default=False)


class Emp_leave_hist(models.Model):
    leave_req = models.ForeignKey(Leave_req, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    

class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    emp_id = models.CharField(verbose_name='employee id', max_length=10, unique=True, default=uuid.uuid4, editable=False)
    staff_id = models.CharField(max_length=10, unique=True)
    f_name = models.CharField(verbose_name='First name', max_length=30)
    l_name = models.CharField(verbose_name='Last name', max_length=30)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEX)
    dept_unit = models.CharField(verbose_name='Department Unit', max_length=30)
    home_addr = models.CharField(verbose_name='Home address', max_length=100)
    designation = models.CharField(verbose_name='Designation', max_length=30)
    phone_num = models.IntegerField(verbose_name='Phone Number',default='0')
    email_addr = models.CharField(verbose_name='Email address', max_length=100)


    def create_profile(self,created,**kwargs):
        if created:
            employee = Employee.objects.create(**kwargs)

    def get_absolute_url(self):
        return reverse(employee.views.EmployeeDetailView, args=[(self.id)])

    def __str__(self):
        return '%s %s' % (self.f_name, self.staff_id)

    

class Dept(models.Model):
    dept_name = models.CharField(verbose_name='Department name', max_length=100)


class Hod(models.Model):
    hod_name = models.CharField(verbose_name='Hod Name', unique=True, max_length=50)
    dept_name = models.ForeignKey('Dept', on_delete=models.CASCADE)


class Superuser(models.Model):
    name = models.CharField(verbose_name='Super_user', max_length=50)
    dept = models.CharField(verbose_name='HR Department', max_length=20)

    def __str__(self):
        return '%s' % (self.name)



