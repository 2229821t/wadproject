from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 128, unique = True, null = False)
    GUID = models.IntegerField(unique = True, null = False)
    email = models.EmailField(max_length = 128, unique = True, null = False)
    password = models.CharField(max_length = 16, null = False)
    nationality = models.CharField(max_length = 128, null = False)
    NLanguge = models.CharField(max_length = 128, null = False)
    NLanguge2 = models.CharField(max_length = 128)
    LLanguge = models.CharField(max_length = 128, null = False)
    LLanguge2 = models.CharField(max_length = 128)

    def _str_(self):
        return name

class Language(models.Model):
    language = models.CharField(max_length = 128, unique = True, null = False)

    def _str_(self):
        return language

class Country(models.Model):
    country = models.CharField(max_length = 128, unique = True, null = False)

    def _str_(self):
        return country

