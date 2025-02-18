from django.urls import path
from .views import aboutus, safe_asli_site, get_post

urlpatterns = [
    path('', safe_asli_site, name='asli'),
    path('aboutus', aboutus, name='aboutus'),
    # path('post/<int:id>', get_post),
]
