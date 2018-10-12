from django.contrib.auth.models import User
from django import forms
 
class UserForm(forms.ModelForm):
    Username = forms.CharField(label='Username')
    Email = forms.EmailField(label='Email')
    Password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['Username', 'Email', 'Password']

        

