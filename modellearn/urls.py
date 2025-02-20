from django.urls import path

from modellearn.views import createPerson

urlpatterns = [
    path('create', createPerson)
]
