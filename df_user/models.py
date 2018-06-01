from django.db import models
# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_legth=20)
    upwd = models.CharField(max_legth=40)
    uemail = models.CharField(max_legth=30)
    ushou = models.CharField(max_legth=20)
    uaddress = models.CharField(max_legth=100)
    uyoubian = models.CharField(max_legth=6)
    uphone = models.CharField(max_legth=16)

