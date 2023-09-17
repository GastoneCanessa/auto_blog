from rest_framework.routers import DefaultRouter
from app.api.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)