from django.db import models

# Create your models here.
class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField()
