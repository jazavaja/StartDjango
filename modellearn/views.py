from django.shortcuts import render

from modellearn.models import Person


# Create your views here.

def createPerson(request):
    # Create Person Model method 1
    Person.objects.create(
        first_name="Javad", last_name="Sarlak", age=27, email="example@example.com",
        username="javadSarlak", mobile="09001001000", description="Javad sarlak teacher django"
    )

    # Create person Model method 2
    # person = Person(first_name="Javad", last_name="Sarlak", age=27, email="example@example.com",
    #                 username="javadSarlak", mobile="09001001000", description="Javad sarlak teacher django")
    # person.save()

