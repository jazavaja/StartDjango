from django.urls import path

from modellearn.views import create_person, update_person, delete_person, read_person,show_register

urlpatterns = [
    path('create', create_person),
    path('show_register', show_register),
    path('read', read_person),
    path('update', update_person),
    path('delete', delete_person),
]
