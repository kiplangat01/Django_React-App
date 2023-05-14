from django.urls import path
from . import views
from .views import PostListView,PostDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about', views.about, name='blog-about'),
    path('register/', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
]
urlpatterns += staticfiles_urlpatterns()
