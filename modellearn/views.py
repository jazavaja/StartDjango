from django.db.models import F, Q
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from modellearn.models import Person


# Create your views here.
def show_register(request):
    return render(request, "register_wf.html")


def profile(request):
    return render(request, 'profile.html')


def get_person_update_after_create(request):
    persons = Person.objects.filter(updated_at__gt=F('create_at'))
    print("---------------")
    for person in persons:
        print(person.first_name)
    print("=============")

    return HttpResponse('')
    pass


def get_person_with_q(request):
    persons = Person.objects.filter(Q(age__lt=30) & Q(sex__exact=1))
    print("-----------")
    for person in persons:
        print(person.first_name)
    print("===========")
    return HttpResponse('')


def create_person(request):
    # Create Person Model method 1
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        try:
            Person.objects.create(
                first_name=first_name, last_name=last_name, age=age, email=email,
                username=username, mobile=mobile, password=password
            )
            return HttpResponse("با موفقیت ایجاد شد")
        except Exception as e:
            return HttpResponse(e)

    return HttpResponse("فقط درخواست POST مجاز است")

    # Create person Model method 2


def read_person(request):
    persons = Person.objects.exclude(age__range=(18, 32)).order_by("-first_name")

    # personnnnn = Person.objects.get(mobile='09001002020')
    # print(personnnnn.first_name)

    return render(request, "read_person.html", {'persons': persons})


def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('read_person')


def update_person(request, id):
    # person = Person.objects.get(id=id)
    person = get_object_or_404(Person, id=id)
    person.age = 300
    person.birthday = timezone.now()

    person.save()
    return redirect('read_person')
