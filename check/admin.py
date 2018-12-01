from django.contrib import admin
from .models import Patient, Profile
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'u', 'first_name', 'last_name')
    fields = ['ssn', ('u', 'first_name', 'last_name'), 'gender']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Profile)