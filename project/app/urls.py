from django.urls import path
from app.views import post_list, create_post

urlpatterns = [
    path('c', create_post, name='create_post'),
    path('list', post_list, name='list'), 
]