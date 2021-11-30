from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

class MediaView(APIView):

    def get(self, request, file, format=None):
        response = Response()
        response['Content-Type'] = ''
        response['X-Sendfile'] = settings.MEDIA_ROOT / file
        return response