from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AbstractUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    zip_code = models.CharField(max_length=12, null=True, blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

class Annotator(models.Model):
    abstract_user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)

class Company(models.Model):
    abstract_user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)

class Dataset():
    issuer = models.ForeignKey(Company,on_delete=models.CASCADE)

class Datum(models.Model):
    container = models.ForeignKey(Dataset,on_delete=models.CASCADE)
    reference = models.CharField(max_length=256)

class Record(models.Model):
    datum = models.ForeignKey(Datum,on_delete=models.SET_NULL,null=True)
    reference = models.CharField(max_length=256)
    points = models.FloatField()
    completed_by = models.ForeignKey(Annotator)