from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about', views.about, name='blog-about'),
    path('register/', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
]
urlpatterns += staticfiles_urlpatterns()
