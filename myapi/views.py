from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi.models import ProductApi
from .serializers import ProductApiSerializer


# Create your views here.

@api_view(['GET'])
def product_list_create(request):
    if request.method == 'GET':
        products = ProductApi.objects.all()
        serial = ProductApiSerializer(products, many=True)
        return Response(serial.data)


class ProductApiListCreate(generics.ListCreateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
