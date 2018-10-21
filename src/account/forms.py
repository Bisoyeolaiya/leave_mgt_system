from django.views.generic import CreateView,FormView
from .models import CustomUser
from django import forms
from django.forms import ModelForm
from django.contrib.auth import (authenticate,get_user_model)
from LMS.employee.models import Employee
 
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class LmsSignUp(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
