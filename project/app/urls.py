from django.urls import path
from app.views import generate_post, post_list

urlpatterns = [
    path('g', generate_post),
    path('', post_list),
]