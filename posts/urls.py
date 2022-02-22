from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/<int:pk>/', PostCreateView.as_view(), name="post_new" ),
] 