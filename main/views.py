from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import QuestionForm, AnswerForm
from main.models import Question, Answer, Vote
from main.tasks import hello_world
from django.utils.translation import gettext_lazy , gettext as _


# Create your views here.

def persian_language(request):
    hello = _('Hi')
    return HttpResponse(f'Persian{hello}')

def english_language(request):
    return HttpResponse('English')

def safe_asli_site(request):
    products = [
        {'id': 1, 'name': 'Samsung 24 Ultra ', 'price': 1000, 'quantity': 10, 'discount': '5 % '},
        {'id': 2, 'name': 'Iphone 15 pro max ', 'price': 2000, 'quantity': 2, 'discount': '10 % '},
        {'id': 3, 'name': 'Xiaomi 17  ', 'price': 1000, 'quantity': 100, 'discount': '30 % '},
    ]
    # hello_world.delay()
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
    questions = Question.objects.prefetch_related('answer_set__vote_set').all()
    return render(request, 'list_questions.html', {"questions": questions})


@login_required
def submit_answer(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        forms = AnswerForm(request.POST)
        if forms.is_valid():
            result_answer = forms.save(commit=False)
            result_answer.author = request.user
            result_answer.question = question
            result_answer.save()
            messages.success(request, "پاسخ شما با موفقیت ثبت شد")
        else:
            for key, values in forms.errors.items():
                for error in values:
                    messages.error(request, error)
            # messages.error(request, 'پاسخ شما کوتاه بوده است لطفا حداقل 10 کاراکتر وارد نمایید')
            pass

    return redirect('list_questions')


@login_required
def plus_vote(request, id):
    answer = get_object_or_404(Answer, id=id)
    user = request.user
    vote_exist = Vote.objects.filter(answer=answer,user=user).first()
    if vote_exist:
        vote_exist.vote_type = 'up'
        vote_exist.save()
    else:
        Vote.objects.create(user=user,answer=answer,vote_type='up')
    return redirect('list_questions')


@login_required
def mines_vote(request, id):
    answer = get_object_or_404(Answer, id=id)
    user = request.user
    vote_exist = Vote.objects.filter(answer=answer,user=user).first()
    if vote_exist:
        vote_exist.vote_type = 'down'
        vote_exist.save()
    else:
        Vote.objects.create(user=user,answer=answer,vote_type='down')
    return redirect('list_questions')
