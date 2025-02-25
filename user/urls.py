from django.urls import path
from .views import UserView, save_session, delete_session, get_session

urlpatterns = [
    path('', UserView.as_view(), name='user_class'),
    path('save_session', save_session, name='save_session'),
    path('delete_session', delete_session, name='delete_session'),
    path('get_session', get_session, name='get_session'),
]
