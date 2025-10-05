from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.home, name='about'),
    path('services.html', views.home, name='services'),
    path('doctors.html', views.home, name='doctors'),
    path('blog.html', views.home, name='blog'),
    path('appointment.html', views.home, name='appointment'),
    path('single.html', views.home, name='single'),
    path('elements.html', views.home, name='elements'),
    
]