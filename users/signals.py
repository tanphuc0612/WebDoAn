from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User

# save to db when sign up 
@receiver(post_save, sender=User)
def create_profile(sender, instance ,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# edit this record in db when edit profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kawrgs):
    instance.profile.save()        