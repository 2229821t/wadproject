from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from LanguageExchange.forms import UserCreationForm,UserChangeForm,SearchForm,MyUserAdmin,MyUserCreationForm
from django.db.models import Q
from LanguageExchange.models import MyUser
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

def about(request):
    about=False
    return render(request, 'LanguageExchange/about.html', {"about":about})
def contact(request):
    return render(request, 'LanguageExchange/contact.html')    
    
def FAQs(request):
    return render(request, 'LanguageExchange/FAQs.html')    
    
def send(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        fromEmail = request.POST.get('fromEmail')
        comment = request.POST.get('comment')
        send_mail(name,comment,fromEmail,['mrsuccess1203@gmail.com'],fail_silently=False)
            
           
    return  HttpResponseRedirect(reverse('contact'))
                  

 
def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = MyUserCreationForm(data=request.POST)
      
        
        print("email")
        if user_form.is_valid():       
           
            user = user_form.save()
            user.save()
                
            if 'Profile_image' in request.FILES:
                    user.Profile_image = request.FILES['Profile_image']
                    user.save()
                    registered = True
        
       
           
        else:   
           messages.warning(request,"Make you sure to use GU ID and Password is more than 8 character", extra_tags='alert') 
           return redirect('/LanguageExchange/')
    else:
        user_form = MyUserCreationForm()
        
    return render(request,
                'LanguageExchange/register.html',
                {'user_form': user_form,
                'registered': registered})
                
                
@login_required                 
def edit(request):
    edited = False
    if request.method == 'POST':
       
        change_form = UserChangeForm(data=request.POST)
        if change_form.is_valid():
           
            #user = change_form.save()
            user = request.user
            user.username = change_form.cleaned_data['username']
            user.set_password(change_form.cleaned_data['password1'])
            user.Mother_language = change_form.cleaned_data['Mother_language']
            user.Wish_language = change_form.cleaned_data['Wish_language']
           
            user.save()
            return redirect('/LanguageExchange/')
           
            
           
       
            edited = True
        
        else: 
           messages.warning(request,"Make you sure to check  Password", extra_tags='alert')
           return redirect('/LanguageExchange/edit')
    else:
       
       
        change_form = UserChangeForm()
    return render(request,
                'LanguageExchange/edit.html',
                {'change_form': UserChangeForm,
                'edited': edited})
                
             
def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
              
                login(request, user)
                return HttpResponseRedirect(reverse('register'))	
           
            else: 
                messages.warning(request,"Make you sure to Check ID and Password", extra_tags='alert') 
                return HttpResponseRedirect(reverse('register'))	
        else:
            messages.warning(request,"Make you sure to Check ID and Password", extra_tags='alert') 
            return HttpResponseRedirect(reverse('register'))	
   
    else:
        messages.warning(request,"Make you sure to Check ID and Password", extra_tags='alert') 
        return HttpResponseRedirect(reverse('register'))	

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))	
        
                

def search(request):
    searched = False
  
    form = SearchForm(request.GET or None) 
    if request.method == "GET" and form.is_valid():
        
        myuser_qs = MyUser.objects.all()
        
        
        Mother_language = form.cleaned_data['Mother_language']
        Nationality = form.cleaned_data['Nationality']
       
        myuser_qs=request.GET.get('q')
        
        myuser_qs = MyUser.objects.filter(Q(Mother_language__contains=Mother_language)|Q(Nationality__contains=Nationality)).distinct()
        
        
        paginator = Paginator( myuser_qs, 5)
        page = request.GET.get('page')
        searched = True
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        
        return render(request, "LanguageExchange/user_list.html",{'Result': users,"searched":searched,})
    
    return render(request, "LanguageExchange/search.html", { "form": form,"searched":searched})
    
    
  