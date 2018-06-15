from django.db import models
from django.db.models import F
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=90, blank=False, unique=False)
    secret = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " / " + str(self.secret)

class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
