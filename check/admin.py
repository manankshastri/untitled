from django.contrib import admin
from .models import MProfile
# Register your models here.

"""
class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'u', 'first_name', 'last_name')
    fields = ['ssn', ('u', 'first_name', 'last_name'), 'gender']


admin.site.register(Patient, PatientAdmin)
"""


@admin.register(MProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_patient', 'is_doctor', 'desc', 'city', 'phone')
    fields = ['user', ('is_patient', 'is_doctor'), ('desc', 'city', 'phone')]