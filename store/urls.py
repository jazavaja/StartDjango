from django.urls import path

from store.views import list_category_view, detail_category_view, delete_category_view, update_category_view, \
    create_category_view, product_list_view, product_update_view, product_create_view, \
    product_delete_view

urlpatterns = [
    path('list_category', list_category_view, name='list_category'),
    path('detail_category_view/<int:id>', detail_category_view, name='detail_category_view'),
    path('update_category/<int:id>', update_category_view, name='update_category_view'),
    path('create_category', create_category_view, name='create_category'),
    path('delete_category/<int:id>', delete_category_view, name='delete_category'),

    path('list_products', product_list_view, name='list_products'),
    path('detail_products_view', product_update_view, name='detail_products_view'),
    path('update_product/<int:id>', product_update_view, name='update_product'),
    path('create_product', product_create_view, name='create_product'),
    path('delete_product/<int:id>', product_delete_view, name='delete_product'),
]
