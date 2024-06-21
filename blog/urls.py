from django.urls import path
from .views import (
    PostDetailView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
   
    
)
from blog import views as blog_views


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>', blog_views.LikeView, name='like_post'),
]