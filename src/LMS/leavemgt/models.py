from django.db import models

# Create your models here.
class Leave_req(models.Model):
    emp_id = models.CharField(verbose_name='employee id', max_length=10, unique=True)
    leave_type = models.ForeignKey('Leave_type', on_delete=models.CASCADE)
    comment = models.TextField(default='include comment here')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')

    STATUS = (
        ('Ap', 'Approved'),
        ('Pn', 'Pending'),
        ('Dn', 'Declined')
    )
    leave_status = models.CharField(verbose_name = 'Leave Request Status', max_length=2, choices=STATUS, default='Pn',editable = False)
    upload = models.FileField(verbose_name='Attach Document',upload_to='uploads/' )

   
    def __str__(self):
        return '%s %s %s' % (self.emp_id, self.leave_type, self.leave_status)
 
    
class Leave_type(models.Model):

    TYPE =(
        ('An', 'Annual leave'),
        ('Pr', 'Proportionate Leave'),
        ('Cs', 'Casual Leave'),
        ('Sk', 'Sick Leave'),
        ('St', 'Study Leave'),
        ('Cm', 'Compulsory Examination'),
        ('Nm', 'Non-compulsory Examination'),
        ('Md', 'Medical Leave'),  
        ('Sb', 'Sabbatical Leave')
    )

    leave_type = models.CharField(verbose_name='Type of leave', max_length=2, choices=TYPE)

    def __str__(self):
        return '%s' % (self.leave_type)
  
