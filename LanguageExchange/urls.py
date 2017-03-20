from django.conf.urls import url
from LanguageExchange import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$',views.edit_information,name='edit'),     
    url(r'^register/$',views.register,name='register'), 
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$',views.about,name='about'),  
    url(r'^contact/$',views.contact,name='contact'),  
    url(r'^send/$', views.send, name = 'send'),
]