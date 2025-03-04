from django import forms

from main.models import Question, Answer, Vote


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title', 'question_description']
        widgets = {
            'question_title': forms.TextInput(attrs={'class': 'form-control'}),
            'question_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_question_title(self):
        title = self.cleaned_data.get('question_title')
        if not title.strip():
            raise forms.ValidationError("عنوان سوال نباید خالی باشد")
        if len(title) < 4:
            raise forms.ValidationError("عنوان سوال نباید کمتر 4 کاراکتر باشد")
        return title

    def clean_question_description(self):
        description = self.cleaned_data.get('question_description')
        if not description.strip():
            raise forms.ValidationError("توضیحات سوال نباید خالی باشد")
        if len(description) < 10:
            raise forms.ValidationError("توضیحات سوال نباید کمتر 10 کاراکتر باشد")
        return description


class AnswerForm(forms.ModelForm):
    content = forms.CharField(
        label="پاسخ",
        widget=forms.Textarea(attrs={'class': 'form_control'}),
        error_messages={
            'required': 'این فیلد الزامی است'
        }
    )

    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form_control'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("پاسخ نباید خالی باشد")
        if len(content) < 10:
            raise forms.ValidationError("پاسخ نباید کمتر 10 کاراکتر باشد")

        return content


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_type']
        widgets = {
            'vote_type': forms.HiddenInput
        }

    def clean(self):
        clean_data = super().clean()
        vote = clean_data.get('vote_type')
        if not vote:
            raise forms.ValidationError('لطفا رای مثبت یا منفی بدهید')

        return clean_data
