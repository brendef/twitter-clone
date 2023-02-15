from django.urls import path 
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('new_post/', views.new_post, name='new_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('upvote/<int:post_id>/', views.upvote, name='upvote'),
    path('downvote/<int:post_id>/', views.downvote, name='downvote'),
]
