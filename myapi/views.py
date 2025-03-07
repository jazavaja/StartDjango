from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from myapi.models import ProductApi, BookApi
from .serializers import ProductApiModelSerializer, ProductApiSerializer, BookSerializer


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


class ProductApiUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiModelSerializer


class ProductGetPostMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiModelSerializer

    def get(self, request, *args, **kwargs):

        name = request.query_params.get('name',None)
        if name:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


def product_print(request):
    product = ProductApi.objects.get(id=6)
    serializer = ProductApiSerializer(data=product.__dict__)
    # print(serializer.initial_data)
    if serializer.is_valid():
        print('saveMethodCall:', serializer.save())
    else:
        print(serializer.errors)
    return HttpResponse('')


def author_detail(request, id):
    return HttpResponse(id)


@api_view(['GET'])
def books_show(request):
    if request.method == 'GET':
        books = BookApi.objects.all()
        serial = BookSerializer(books, many=True, context={'request': request})
        return Response(serial.data)


class BookApiListCreateView(APIView):
    def get(self, request):
        name= request.query_params.get('name',None)
        if name:
            books = BookApi.objects.filter(author__name__contains=name)
        else:
            books = BookApi.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serial = BookSerializer(data=request.data)
        if serial.is_valid():
            b = serial.save()
            return Response(BookSerializer(b, context={'request': request}).data, status=HTTP_201_CREATED)
        return Response(serial.errors, status=HTTP_400_BAD_REQUEST)


class BookApiListAuto(viewsets.ModelViewSet):
    queryset = BookApi.objects.all()
    serializer_class = BookSerializer
