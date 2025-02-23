from django.urls import path

from store.views import list_category_view, detail_category_view, delete_category_view, update_category_view, \
    create_category_view

urlpatterns = [
    path('list_category', list_category_view, name='list_category'),
    path('detail_category_view/<int:id>', detail_category_view, name='detail_category_view'),
    path('update/<int:id>',update_category_view, name='update_category_view'),
    path('create_category',create_category_view, name='create_category'),
    path('delete_category/<int:id>', delete_category_view, name='delete_category')
]
