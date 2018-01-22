from snippets.serializers import SnippetSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
# Create your views here.

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

