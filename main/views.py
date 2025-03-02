from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main.forms import QuestionForm
from main.models import Question


# Create your views here.

def safe_asli_site(request):
    products = [
        {'id': 1, 'name': 'Samsung 24 Ultra ', 'price': 1000, 'quantity': 10, 'discount': '5 % '},
        {'id': 2, 'name': 'Iphone 15 pro max ', 'price': 2000, 'quantity': 2, 'discount': '10 % '},
        {'id': 3, 'name': 'Xiaomi 17  ', 'price': 1000, 'quantity': 100, 'discount': '30 % '},
    ]
    return render(request, 'index.html', {'products': products})


def aboutus(request):
    # return ""
    return render(request, "aboutus.html")


def get_post(request, id):
    return ""
    # return render(request, 'post_get.html', {'id': id})


@login_required
def submit_question(request):
    if request.method == "POST":
        forms = QuestionForm(request.POST)
        if forms.is_valid():
            question = forms.save(commit=False)
            question.author = request.user
            question.save()
    else:
        forms = QuestionForm()
    return render(request, 'question.html', {'forms': forms})
    pass


@login_required
def list_questions(request):
    questions = Question.objects.all()

    return render(request, 'list_questions.html', {"questions": questions})

def submit_answer(request, id):
    pass