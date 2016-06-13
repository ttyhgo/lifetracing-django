from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gps, name ='gps'),
    url(r'^data/', views.data, name='data')
]