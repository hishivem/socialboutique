from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

# Create your models here.


class Joinus(models.Model):
    name = models.CharField(max_length=80, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.CharField(max_length=180, null=True, blank=False)

    def __str__(self):
        return self.name


class Yourrequirements(models.Model):
    name = models.CharField(max_length=80, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.CharField(max_length=180, null=True, blank=False)
    requirements = models.ManyToManyField("Requirement")

    def __str__(self):
        return self.name


class Requirement(models.Model):
    name = models.CharField(max_length=300, null=True, blank=False)

    def __str__(self):
        return self.name
