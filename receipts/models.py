from django.conf import settings
from django.db import models
import PIL
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model, admin

# Create your models here.

User = get_user_model()


def upload_image(instance, filename):
    return "receipts/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass

class ReceipManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

User = get_user_model()


class Receipts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=256)
    ingredients = models.CharField(max_length=256)
    image_main = models.ImageField(upload_to=upload_image, null= True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = ReceipManager()

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()


    def get_absolute_url(self):
        return reverse("receipts:detail",kwargs={'pk':self.pk})
    # def get_absolute_url(self):
    #     return reverse('home')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]



class ReceiptSteps(models.Model):
    id_receipts = models.ForeignKey(Receipts)
    description = models.CharField(max_length=256)
    image = models.ImageField()


# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User)
