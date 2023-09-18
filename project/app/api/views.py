from rest_framework import viewsets
from app.models import Post
from app.api.serializers import PostSerializer
from app.api.permissions import ReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [ReadOnlyPermission]