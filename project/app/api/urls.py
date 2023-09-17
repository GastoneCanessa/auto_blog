from django.urls import path, include
from app.api.routers import router

urlpatterns = [
    path('', include(router.urls)),
]