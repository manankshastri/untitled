from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.user}'


class Patient(models.Model):
    """for patient"""
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
        """Returns the url to access a detail record for this book."""
        return reverse('patient_detail', args=[str(self.ssn)])