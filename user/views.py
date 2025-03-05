from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from user.forms import ProfileForm
from user.models import User, Profile


# Create your views here.

def create_user_custom(request):
    User.objects.create_user('111juju@juju.com', '445566778899')
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


@login_required
def show_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
            return redirect('profile')
    else:
        forms = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'forms': forms})
