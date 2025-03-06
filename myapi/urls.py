from django.urls import path

from myapi.views import product_list_create, ProductApiListCreate, product_print, books_show, author_detail, \
    BookApiListCreateView

urlpatterns = [
    path('list_products', product_list_create, name="product_list_create"),
    path('class_list_products', ProductApiListCreate.as_view(), name="class_list_products"),
    path('product_print', product_print, name='product_print'),
    path('books', books_show, name='books_show'),
    path('author_detail/<int:id>', author_detail, name="author_detail"),
    path('book_class',BookApiListCreateView.as_view(),name='book_class')
]
