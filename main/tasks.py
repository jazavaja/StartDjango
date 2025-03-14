import time

from celery import shared_task


@shared_task
def hello_world():
    time.sleep(10)
    print('Hello World')
    time.sleep(20)
    print("Next hello world")


@shared_task
def add_two_numbers(x, y):
    return x + y
