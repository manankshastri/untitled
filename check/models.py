from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class MProfile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', "Female")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        mprofile = MProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)