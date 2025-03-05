from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import UserView, save_session, delete_session, get_session, create_user_custom, show_profile, edit_profile

urlpatterns = [
    path('', UserView.as_view(), name='user_class'),
    path('save_session', save_session, name='save_session'),
    path('delete_session', delete_session, name='delete_session'),
    path('get_session', get_session, name='get_session'),
    path('create_user_custom', create_user_custom, name='create_user_custom'),
    path('show_profile', show_profile, name="show_profile"),
    path('edit_profile', edit_profile, name='edit_profile')
]

