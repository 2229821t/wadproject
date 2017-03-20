from django.contrib import admin
from django import forms
from LanguageExchange.models import UserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Type Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'RE-Type Password', widget = forms.PasswordInput)
    
    class Meta:
        model = UserProfile
        fields = ['GUemail','Name','Nationality','Mother_language','Wish_language',]
        
        def clean_password2(self):
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password1']
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError('Password does not match.')
            return password2
            
        def save(self, commit = True):
            user = Super(UserCreationForm,self).save(commit =False)
            user.ser_password(self.cleaned_data['password1'])
            user.save()
            return user
            
            
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = UserProfile 
        fields = ('GUemail','Name','Nationality','Mother_language','Wish_language',)
    def clean_password(seld):
        return self.initial['password']
        
        
class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ['GUemail','Name','Nationality','Mother_language','Wish_language','is_super', ]
    ordering = ['GUemail',]
    
admin.site.register(UserProfile,UserProfileAdmin)