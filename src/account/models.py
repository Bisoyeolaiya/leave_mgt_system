from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,staff_id,password=None,is_active=True,is_staff =False,is_hod = False,is_director = False,is_admin = False):
        if not staff_id:
            raise ValueError("user must have valid staff id")

        if not password:
            raise ValueError("user must have password")

        user_obj = self.model(
            staff_id = self.staff_id
        )
        user_obj.set_password(password)

        user_obj.active = self.is_active
        user_obj.staff = self.is_staff
        user_obj.hod = self.is_hod
        user_obj.director = self.is_director
        user_obj.save(using = self._db)

        return user_obj

    def create_staffuser(self,staff_id,password):
        user = self.create_user(
            staff_id,
            password=password,
            is_staff=True
        )
        return user

    
    def create_hod(self,staff_id,password):
        user = self.create_user(
            staff_id,
            password=password,
            is_staff = True,
            is_hod=True
        )
        return user

        
    def create_director(self,staff_id,password):
        user = self.create_user(
            staff_id,
            password=password,
            is_staff = True,
            is_hod=True,
            is_director=True
        )
        return user


        
    def create_admin(self,staff_id,password):
        user = self.create_user(
            staff_id,
            password=password,
            is_staff = True,
            is_hod=True,
            is_director=True,
            is_admin= True
        )
        return user

    
    
    
            


class CustomUser(AbstractBaseUser):
    staff_id = models.CharField(max_length = 50,unique = True)
    active  = models.BooleanField(default = True)
    staff = models.BooleanField(default = True)
    hod = models.BooleanField(default = False)
    director = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'staff_id'

    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.staff_id

    def get_full_name(self):
        return self.staff_id

    def get_short_name(self):
        return self.staff_id

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


