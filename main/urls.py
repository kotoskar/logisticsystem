from django.urls import path
from . import views

urlpatterns = [
    path('', views.usermode, name='usermode'),
    path('main.html', views.usermode, name='usermode'),
    path('send/', views.send, name='senddata'),
    path('about.html', views.about, name='usermode'),
    path('abouteng.html', views.abouteng, name='usermode')
]
