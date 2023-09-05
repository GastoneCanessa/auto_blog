from django.urls import path
from app.views import generate_post

urlpatterns = [
    path('', generate_post),
]