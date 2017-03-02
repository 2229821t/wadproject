from django.conf.urls import url
from LanguageExchange import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]