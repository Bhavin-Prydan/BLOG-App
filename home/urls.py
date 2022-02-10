from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('contact', views.contact, name='contact'),
     path('search', views.search, name='search'),
     path('signup', views.handlesignup, name='handlesignup'),
     path('login', views.handlelogin, name='handlelogin'),
     path('logout', views.handlelogout, name='handlelogout'),
     path("password_reset", views.password_reset_request, name="password_reset"),
]
