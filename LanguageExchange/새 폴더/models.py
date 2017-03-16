from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import models as auth_models 

from django.template.defaultfilters import slugify


class CustomUserManager(auth_models.BaseUserManager):
    def create_user(self,GUemail,Password,Name,Nationality,Mother_language,Wish_Language,):
        
      
        user = self.model(
        
                            GUemail = CustomUserManager.nomalize_email(email),
                            Name=Name,
                            Nationality=Nationality,
                            Mother_language=Mother_language,
                            Wish_Language=Wish_Language
        )
        user.is_staff=True
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,GUemail,Password,Name,Nationality,Mother_language,Wish_Language):

        user = self.model(
        
                            GUemail = CustomUserManager.nomalize_email(email),
                            Name=Name,
                            Nationality=Nationality,
                            Mother_language=Mother_language,
                            Wish_Language=Wish_Language
        )
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserProfile(auth_models.AbstractBaseUser):
      
      GUemail = models.EmailField(unique=True)
      Name = models.CharField(max_length = 30, unique = True, null = False)
      Nationality = models.CharField(max_length = 128, null = False)
      Mother_language = models.CharField(max_length = 128, null = False)
      Wish_language = models.CharField(max_length = 128, null = False)
      is_staff = models.BooleanField()
      
      USERNAME_FIELD='GUemail'
      REQUIRED_FIELD=['Name','Nationality','Mother_language','Wish_language',]
      
      
      def get_full_ID(self):
        return self.GUemail
        
      def is_staff(self):
        return self.is_staff











