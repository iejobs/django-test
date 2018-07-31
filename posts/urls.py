from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]