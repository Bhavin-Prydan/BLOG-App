from django.urls import path
from . import views
urlpatterns = [
	 path('postcomment', views.postcomment, name='postcomment'),
     path('', views.blogHome, name='blogHome'),
     path('<str:slug>', views.blogPost, name='blogPost'),
    
]
