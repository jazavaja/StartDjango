from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

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
