from rest_framework import authentication
from video.models import Video
from .serializers import VideoSerializer
from rest_framework import viewsets


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Video.objects.all()
