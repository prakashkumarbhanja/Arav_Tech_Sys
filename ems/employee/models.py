from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model): #9
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{} {} {}".format(self.user.first_name, self.user.last_name, self.id)


@receiver(post_save, sender=User)
def user_created_or_updated(sender, instance, created, **kwargs):#This method is for receiving the signal
    if created: # if no then this block will execute or else block will exicute...
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()