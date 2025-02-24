from django.contrib.auth.forms import UserCreationForm
from django import forms

from modellearn.models import Person


class PersonForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Person
        fields = ('email', 'username', 'last_name', 'first_name', 'age')
