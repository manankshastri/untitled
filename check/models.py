from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class MProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    desc = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

"""
class Patient(models.Model):
   #  for patient
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    u = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    ssn = models.IntegerField('SSN', blank=False)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.ssn)])

"""


def create_profile(sender, **kwargs):
    if kwargs['created']:
        mprofile = MProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)