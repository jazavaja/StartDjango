from django.urls import path

from .views import aboutus, safe_asli_site, submit_question, list_questions, submit_answer

urlpatterns = [
    path('', safe_asli_site, name='asli'),
    path('aboutus', aboutus, name='aboutus'),
    path('questions', submit_question, name='submit_question'),
    path('list_questions', list_questions, name='list_questions'),
    path('submit_answer/<int:id>',submit_answer,name='submit_answer')
    # path('post/<int:id>', get_post),
]
