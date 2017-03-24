from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from LanguageExchange.models import MyUser

class SearchForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('Mother_language','Nationality')



class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}) )
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
   
    
    class Meta:
        model = MyUser
        def __init__(self, auto_id='%s', *args, **kwargs):
            super(Meta, self).__init__(*args, **kwargs)
            self.fields['Mother_language'].choices = ('','Please choose ') + models.Language_list
            self.fields['Mother_language'].choices = ('','Please choose ') + models.Language_list
        widgets = {
            'email': forms.TextInput(attrs={'size':30,'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'size':30,'placeholder': 'UserName'}),
            'status_message': forms.TextInput(attrs={'height':50,'placeholder': 'Write your message'}),
            
        }
        
        fields = ('email','username','Mother_language','Nationality','Wish_language','Profile_image','status_message')
        
        

        

    
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        elif  len(password1) < 8:
            raise forms.ValidationError('Password too short, more than 8 charecters')
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
        fields = (  'username','Mother_language','Wish_language','Profile_image','status_message')

    def clean(self):
            if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                    raise forms.ValidationError(_("Password does not match!"))
                elif len(self.cleaned_data['password1']) < 8:
                    raise forms.ValidationError('Password too short, more than 8 charecters')
            return self.cleaned_data
     
    def save(self, commit=True):
            UserUpdate = super(UserChangeForm, self).save(commit=False)
            UserUpdate.set_password=self.cleaned_data['password1']
            UserUpdate.Mother_language = self.cleaned_data['Mother_language']
            UserUpdate.Wish_language = self.cleaned_data['Wish_language']

    
 
      



class MyUserAdmin(UserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm
    serach = SearchForm
   
    list_display = ('email', 'username','Nationality','Mother_language','Wish_language', 'Profile_image','status_message','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','Nationality','Mother_language','Wish_language','Profile_image','status_message')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','Nationality','Mother_language','Wish_language','Profile_image','status_message', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username','Nationality','Mother_language','Wish_language','Profile_image','status_message', 'password')
    ordering = ('email',)
    filter_horizontal = ()
    

class MyUserCreationForm(UserCreationForm):
    def clean_email(self):
        if not self.cleaned_data['email'].endswith('gla.ac.uk'):
           raise forms.ValidationError('You need to use GU ID')
        return self.cleaned_data['email']
        
    def clean_unsername(self):
        
        return self.cleaned_data['username'].upper()
    
    
   