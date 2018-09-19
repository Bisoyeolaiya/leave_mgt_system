from django.db import models
from LMS.leavemgt.models import Leave_req
import uuid

# Create your models here.

class Hod_approved(models.Model):
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    dept_name = models.ForeignKey('Dept', on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)


class Emp_leave_hist(models.Model):
    leave_req = models.ForeignKey(Leave_req, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    

class Employee(models.Model):
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
    phone_num = models.IntegerField(verbose_name='Phone Number', unique=True)
    email_add = models.CharField(verbose_name='Email address', unique=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.f_name, self.staff_id)

class Dept(models.Model):
    dept_name = models.CharField(verbose_name='Department name', max_length=100)
    hod_name = models.ForeignKey('Hod', on_delete=models.CASCADE)


class Hod(models.Model):
    hod_name = models.CharField(verbose_name='Hod Name', unique=True, max_length=50)
    dept_name = models.ForeignKey('Dept', on_delete=models.CASCADE)


class Superuser(models.Model):
    name = models.CharField(verbose_name='Super_user', max_length=50)
    dept = models.CharField(verbose_name='HR Department', max_length=20)

    def __str__(self):
        return '%s' % (self.name)



        



    



        

