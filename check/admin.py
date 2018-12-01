from django.contrib import admin
from .models import Patient, Profile
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'u', 'first_name', 'last_name')
    fields = ['ssn', ('u', 'first_name', 'last_name'), 'gender']


admin.site.register(Patient, PatientAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_patient', 'is_doctor')
    fields = ['user', 'is_patient', 'is_doctor']