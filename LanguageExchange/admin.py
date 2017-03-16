#-*- coding: utf-8 -*-
from django import forms
from django.contrib import admin



from LanguageExchange.models import MyUser
from LanguageExchange.forms import MyUserAdmin


admin.site.register(MyUser, MyUserAdmin)
