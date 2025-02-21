from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from modellearn.models import Person


# Create your views here.
def show_register(request):
    User.objects.create()
    return render(request, "register.html")


def create_person(request):
    # Create Person Model method 1
    # if request.method == "POST":

    try:
        Person.objects.create(
            first_name="Javad", last_name="Sarlak", age=27, email="example34@example.com",
            username="javadSarlak11", mobile="09001301000", password="123456"
        )
        return HttpResponse("با موفقیت ایجاد شد")
    except Exception as e:
        return HttpResponse(e)

    # return HttpResponse("فقط درخواست POST مجاز است")

    # Create person Model method 2



def read_person(request):
    pass


def delete_person(request):
    pass


def update_person(request):
    pass
