from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from LanguageExchange.models import MyUser

class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username','Nationality','Mother_language','Wish_language','picture')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = MyUser
        fields = (  'Mother_language','Wish_language','picture')

    def clean(self):
            if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError(_("Password does not match!"))
            return self.cleaned_data

    def save(self, commit=True):
            UserUpdate = super(UserChangeForm, self).save(commit=False)
            UserUpdate.set_password=self.cleaned_data['password1']
            UserUpdate.Mother_language = self.cleaned_data['Mother_language']
            UserUpdate.Wish_language = self.cleaned_data['Wish_language']

    
   
      



class MyUserAdmin(UserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm

   
    list_display = ('email', 'username','Nationality','Mother_language','Wish_language', 'picture','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','Nationality','Mother_language','Wish_language','picture')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','Nationality','Mother_language','Wish_language','picture', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username','Nationality','Mother_language','Wish_language','picture', 'password')
    ordering = ('email',)
    filter_horizontal = ()
