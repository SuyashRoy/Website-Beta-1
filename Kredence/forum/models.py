from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

"""----------------------------------------------Discussion Model----------------------------------------------------"""
class Discussion(models.Model):
    user = models.ForeignKey(User , max_length=30, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slug)

@receiver(pre_save, sender=Discussion)
def pre_save_discussion_reciever(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username + '-' + instance.title)

pre_save.connect(pre_save_discussion_reciever, sender=Discussion)


"""----------------------------------------------Answer Model--------------------------------------------------------"""
class Answer(models.Model):
    discussion = models.ForeignKey(Discussion, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    answer = models.TextField(max_length=3000, blank=True, null=True)
    votes = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slug)


@receiver(pre_save, sender=Answer)
def pre_save_answer_reciever(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username + '-answer-to-' + instance.discussion.title)

pre_save.connect(pre_save_answer_reciever, sender=Answer)