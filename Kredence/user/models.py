from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

Social_Network = {
    ('facebook','Facebook'),
    ('instagram','Instagram'),
    ('linkedin','LinkedIn'),
    ('github','Github')
}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    social_link_1 = models.URLField(max_length=200, choices=Social_Network, unique=True, blank=True, null=True)
    social_link_2 = models.URLField(max_length=200, choices=Social_Network, unique=True, blank=True, null=True)

    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
