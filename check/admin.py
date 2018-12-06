from django.contrib import admin
from .models import MProfile
# Register your models here.


@admin.register(MProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    fields = ['user', 'phone']