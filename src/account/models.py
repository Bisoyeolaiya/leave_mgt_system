from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,staff_id,first_name,last_name,sex,department_unit,home_address,email_addr,designation,password=None,is_active=True,is_staff =False,is_hod = False,is_director = False,is_admin = False):
        if not staff_id:
            raise ValueError("user must have valid staff id")

        if not password:
            raise ValueError("user must have password")

        user_obj = self.model(
            staff_id = staff_id,
            first_name = first_name,
            last_name = last_name,
            sex=sex,
            department_unit = department_unit,
            home_address = home_address,
            email_addr = email_addr,
            designation = designation
        )
        user_obj.set_password(password)

        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.hod = is_hod
        user_obj.director = is_director
        user_obj.admin = is_admin
        user_obj.save(using = self._db)

        return user_obj

    def create_staffuser(self,staff_id,first_name,last_name,sex,department_unit,email_addr,home_address,designation,password):
        user = self.create_user(
            staff_id,
            password=password,
            first_name = first_name,
            last_name = last_name,
            sex=sex,
            department_unit = department_unit,
            home_address = home_address,
            email_addr = email_addr,
            designation = designation,
            is_staff=True
        )
        return user

    
    def create_hod(self,staff_id,first_name,last_name,sex,department_unit,email_addr,home_address,designation,password):
        user = self.create_user(
            staff_id,
            password=password,
            first_name = first_name,
            last_name = last_name,
            sex=sex,
            department_unit = department_unit,
            home_address = home_address,
            email_addr = email_addr,
            designation = designation,
            is_staff=True,
            is_hod = True
        )
        return user

        
    def create_director(self,staff_id,first_name,last_name,sex,department_unit,home_address,email_addr,designation,password):
        user = self.create_user(
            staff_id,
            first_name = first_name,
            last_name = last_name,
            sex=sex,
            department_unit = department_unit,
            home_address = home_address,
            email_addr = email_addr,
            designation = designation,
            password=password,
            is_staff = True,
            is_director=True
        )
        return user


        
    def create_superuser(self,staff_id,first_name,last_name,sex,department_unit,home_address,email_addr,designation,password):
        user = self.create_user(
            staff_id,
            password=password,
            first_name = first_name,
            last_name = last_name,
            sex = sex,
            department_unit = department_unit,
            home_address = home_address,
            designation = designation,
            email_addr = email_addr,
            is_staff = True,
            is_admin= True
        )
        return user

    

class CustomUser(AbstractBaseUser):

    staff_id = models.CharField(max_length = 20,unique = True)
    first_name = models.CharField(verbose_name='First name', max_length=30,default = '')
    last_name = models.CharField(verbose_name='Last name', max_length=30,default = '')
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEX,default='M')
    department_unit = models.CharField(verbose_name='Department Unit', max_length=30,default = '')
    home_address = models.CharField(verbose_name='Home address', max_length=100,default = '')
    designation = models.CharField(verbose_name='Designation', max_length=30,default = '')
    email_addr = models.CharField(verbose_name='Email address',max_length=100,default = 'abc@gmail.com')

    active  = models.BooleanField(default = False)
    staff = models.BooleanField(default = True)
    hod = models.BooleanField(default = False)
    director = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'staff_id'

    REQUIRED_FIELDS = ['first_name','last_name','sex','department_unit','home_address','email_addr','designation']

    object = CustomUserManager()

    def __str__(self):
        return self.staff_id

    def get_full_name(self):
        return self.staff_id

    def get_short_name(self):
        return self.staff_id

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_director(self):
        return self.director

    @property
    def is_hod(self):
        return self.hod
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    object = CustomUserManager()


