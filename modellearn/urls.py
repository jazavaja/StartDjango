from django.urls import path

from modellearn.views import create_person, update_person, delete_person, read_person, show_register

urlpatterns = [
    path('create', create_person, name='create_person'),
    path('show_register', show_register , name='show_register'),
    path('read', read_person, name='read_person'),
    path('update/<int:id>', update_person, name="update_person"),
    path('delete/<int:id>', delete_person, name='delete_person'),
]
