from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="نام", required=True, max_length=100)
    email = forms.EmailField(label="ایمیل", required=True)
    message = forms.CharField(label="پیام", required=True, widget=forms.Textarea)
