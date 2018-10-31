# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import LmsSignUp, UserAdminChangeForm
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = LmsSignUp

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('staff_id','active','staff','hod','director','admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('staff_id', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','sex','department_unit','home_address','designation')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('staff_id', 'password1', 'password2')}
        ),
    )
    search_fields = ('staff_id',)
    ordering = ('staff_id',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
