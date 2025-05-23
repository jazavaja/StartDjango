from django.urls import path

from modellearn.views import create_person, update_person, delete_person, read_person, show_register, \
    get_person_update_after_create, get_person_with_q, register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create', create_person, name='create_person'),
    path('show_register_wf', show_register, name='show_register_wf'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('register', register, name="register"),
    path('profile', profile, name='profile'),
    path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('read', read_person, name='read_person'),
    path('update/<int:id>', update_person, name="update_person"),
    path('delete/<int:id>', delete_person, name='delete_person'),
    path('person_who_update', get_person_update_after_create, name='person_who_update'),
    path('get_person_with_q', get_person_with_q, name='get_person_with_q')
]
