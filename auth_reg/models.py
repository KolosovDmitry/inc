from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    count_job = models.IntegerField(max_length=2000, blank=True)
    class Meta:
        permissions = (
            ("can_view_url", "Может видеть пункты меню"),
            )
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	#for user in User.objects.all():
		#User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
		#Profile.objects.get_or_create(user=user)

	if created:
		Profile.objects.create(user=instance)
		#User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
		#Profile.objects.get_or_create(user=user)
		
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()