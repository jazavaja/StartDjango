from django.urls import path

from myapi.views import product_list_create, ProductApiListCreate, product_print

urlpatterns = [
    path('list_products', product_list_create, name="product_list_create"),
    path('class_list_products', ProductApiListCreate.as_view(), name="class_list_products"),
    path('product_print',product_print,name='product_print')
]
