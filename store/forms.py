from django import forms

from store.models import Product, Category


class ContactForm(forms.Form):
    name = forms.CharField(label="نام", required=True, max_length=100)
    email = forms.EmailField(label="ایمیل", required=True)
    message = forms.CharField(label="پیام", required=True, widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
