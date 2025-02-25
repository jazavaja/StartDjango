from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from user.models import User


# Create your views here.

def create_user_custom(request):
    User.objects.create_user('111juju@juju.com','445566778899')
    return HttpResponse('')
def save_session(request):
    request.session['username'] = "JavadSarlak"
    return HttpResponse('')


def delete_session(request):
    if "username" in request.session:
        del request.session['username']
    return HttpResponse('')


def clear_session(request):
    request.session.flush()
    return HttpResponse('')


def get_session(request):
    result = request.session.get('username', None)
    return HttpResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request):
        return HttpResponse(f"Get User")

    def post(self, request):
        return HttpResponse(f"post User")

    def put(self, request):
        return HttpResponse(f"put User")

    def delete(self, request):
        return HttpResponse(f"delete User")
