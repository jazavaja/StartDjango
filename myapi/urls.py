from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from myapi.views import product_list_create, ProductApiListCreate, product_print, author_detail, \
    BookApiListAuto

routers = DefaultRouter()
routers.register('books', BookApiListAuto)

urlpatterns = [
    path('list_products', product_list_create, name="product_list_create"),
    path('class_list_products', ProductApiListCreate.as_view(), name="class_list_products"),
    path('product_print', product_print, name='product_print'),
    # path('books', books_show, name='books_show'),
    path('author_detail/<int:id>', author_detail, name="author_detail"),
    # path('book_class',BookApiListCreateView.as_view(),name='book_class'),
    # path('book_class',BookApiListAuto.as_view(),name='book_class'),
    path('', include(routers.urls))
]
