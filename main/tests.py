from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from modellearn.models import Person
from .models import Question, Answer


# Create your tests here.
# def add(x,y)
#     return x+y

def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


class TestMath(TestCase):
    def setUp(self) -> None:
        pass

    def test_addition(self):
        result = add(2, 4)
        self.assertEqual(result, 6)

    def test_subtraction(self):
        result = subtraction(4, 4)
        self.assertEqual(result, 0)
        pass


class TestAnswer(TestCase):
    def setUp(self):
        self.author = Person.objects.create(username="javad", email="jon@jo.com")
        self.question = Question.objects.create(
            author=self.author,
            question_title="JAVAD",
            question_description="SARLAK",
            status=False
        )

    # def test_question(self):
    #     question_data = {
    #         'author': self.author,
    #         'question_title': "Title",
    #         'question_description': 'sarlak',
    #     }
    #     question = Question(**question_data)
    #     with self.assertRaises(ValidationError) as c:
    #         question.full_clean()
    #     print(c.exception)
    #     with self.assertRaises(IntegrityError):
    #         question.save()
    #     self.assertEqual(question.question_title, 'javad')

    def test_answer(self):
        answer_data = {
            "question": self.question,
            # "author": self.author,
            "content":"Test",
            "status": True,
        }
        answer = Answer(**answer_data)
        with self.assertRaises(ValidationError) as contextError:
            answer.full_clean()
        print("Why Validation Error :",contextError.exception)
        with self.assertRaises(IntegrityError) as contextError2:
            answer.save()
        print("Why IntegrityError Error :",contextError2.exception)

