from django.urls import path 
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('upvote/<int:post_id>/', views.upvote, name='upvote'),
    path('downvote/<int:post_id>/', views.downvote, name='downvote'),
]
