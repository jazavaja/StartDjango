from django.db import models

from modellearn.models import Person


# Create your models here.

class Question(models.Model):
    question_title = models.CharField(max_length=100)
    question_description = models.TextField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, verbose_name='وضعیت فعال بودن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = "پرسش"
        verbose_name_plural = "پرسشها"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.BooleanField(default=False, verbose_name='وضعیت فعال بودن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")


class Vote(models.Model):
    vote_tuple = (
        ('up', 'رای مثبت'), ('down', 'رای منفی'),
    )
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question,on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=vote_tuple)
