from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(AbstractUser):

    def _try_create_profile_for_user(self, created):
        if created:
            Profile.objects.get_or_create(user=self)

    def save(self, *args, **kwargs):

        created = self.id is None

        self.username = f'demo_{self.username}'

        super(MyUser, self).save(*args, **kwargs)

        self._try_create_profile_for_user(created)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    address = models.TextField(default='')
