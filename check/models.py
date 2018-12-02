from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class MProfile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', "Female")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    desc = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    phone = models.IntegerField(default=0)
    ssn = models.IntegerField(default=0, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        mprofile = MProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)