from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi.models import ProductApi
from .serializers import ProductApiModelSerializer, ProductApiSerializer


# Create your views here.

@api_view(['GET'])
def product_list_create(request):
    if request.method == 'GET':
        products = ProductApi.objects.all()
        serial = ProductApiModelSerializer(products, many=True)
        return Response(serial.data)


class ProductApiListCreate(generics.ListCreateAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiModelSerializer


def product_print(request):
    product = ProductApi.objects.get(id=6)
    serializer = ProductApiSerializer(data=product.__dict__)
    # print(serializer.initial_data)
    if serializer.is_valid():
        print('saveMethodCall:', serializer.save())
    else:
        print(serializer.errors)
    return HttpResponse('')
