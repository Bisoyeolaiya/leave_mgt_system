
from .models import CustomUser
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from LMS.employee.models import Employee

class LoginForm(forms.Form):
    staff_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        staff_id = self.cleaned_data.get('staff_id')
        password = self.cleaned_data.get('password')

        if staff_id and password:
            user = authenticate(username = staff_id, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)
 

class LmsSignUp(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta():
        model = CustomUser
        fields = ('__all__')
        
        
    def clean_staffId(self):
        staff_id = self.cleaned_data.get('staff_id')
        qs = CustomUser.objects.filter(staff_id = staff_id)
        if qs.exist():
            raise forms.ValidationError("Invalid Staff Id")


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(LmsSignUp, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('staff_id', 'password', 'active','staff','hod','director','admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LMSRegForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('__all__')
