from django.db import models
from LMS.employee.models import Employee,Superuser,Hod,Dept
# Create your models here.

class General(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    super_user = models.ForeignKey(Superuser, on_delete=models.CASCADE)
    hod_id = models.ForeignKey(Hod, on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE)
    director = models.BooleanField(default=False)
    
    hrAdmin = models.BooleanField(default=False)
    


    def __str__(self):
        return '%s %s' % (self.emp_id, self.dept_id)
