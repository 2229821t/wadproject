from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from languages.fields import LanguageField
from django_countries.fields import CountryField

class MyUserManager(BaseUserManager):
    def create_user(self, email,username,Nationality,Mother_language,Wish_language,picture,password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            picture=picture,
            Nationality=Nationality,
            Mother_language=Mother_language,
            Wish_language=Wish_language
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,Nationality,Mother_language,Wish_language,password,picture):
       
        user = self.create_user(email,
            password=password,
            username=username,
            picture=picture,
            Nationality=Nationality,
            Mother_language=Mother_language,
            Wish_language=Wish_language,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length = 30, unique = True, null = False)
   
    Nationality =CountryField()
    Mother_language = LanguageField()
    Wish_language = LanguageField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','Nationality','Mother_language','Wish_language','picture']

    def set_picture(self):
       self.has_picture = True
    
    def get_full_name(self):
       
        return self.email

    def get_short_name(self):
       
        return self.email

    def __str__(self):             
        return self.email

    def has_perm(self, perm, obj=None):
       
        return True

    def has_module_perms(self, app_label):
        
        return True

    @property
    def is_staff(self):
       
        return self.is_admin
