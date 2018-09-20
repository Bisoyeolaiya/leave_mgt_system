from django.db import models
# Create your models here.
  
class Leave_req(models.Model):


    LEAVE_TYPE =(
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

    emp_id = models.CharField(verbose_name='employee id', max_length=10, unique=True)
    leavetype = models.CharField(verbose_name='Type of leave', max_length=2, choices=LEAVE_TYPE,default='An')
    comment = models.TextField(default='include comment here')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')


    STATUS = (
        ('Ap', 'Approved'),
        ('Pn', 'Pending'),
        ('Dn', 'Declined')
    )
    leave_status = models.CharField(verbose_name = 'Leave Request Status', max_length=2, choices=STATUS, default='Pn')
    upload = models.FileField(verbose_name='Attach Document',upload_to='uploads/' )

   
    def __str__(self):
        return '%s %s %s' % (self.emp_id, self.leavetype, self.leave_status)
 
    
