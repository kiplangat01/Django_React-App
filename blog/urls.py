from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('register/', views.register, name='register')
]
urlpatterns += staticfiles_urlpatterns()
