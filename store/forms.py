from django import forms

from store.models import Product, Category


def forbidden_email(value):
    forbidden_email = ['admin@example.com', 'info@example.com']
    if value.lower() in forbidden_email:
        raise forms.ValidationError('Please do not use email our site')
    pass


class ContactForm(forms.Form):
    name = forms.CharField(label="نام", required=True, max_length=100)
    email = forms.EmailField(label="ایمیل", required=True, widget=forms.EmailInput, validators=[forbidden_email])
    message = forms.CharField(label="پیام", required=True, widget=forms.Textarea)

    # age = forms.IntegerField(required=False, min_value=18, max_value=99)
    # password = forms.CharField(required=True, widget=forms.PasswordInput)
    # password_confirm = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Please Use Gmail for Contact')
        return email

    def clean(self):
        clean_data = super().clean()
        # password = clean_data.get('password')
        # password_confirm = clean_data.get('password_confirm')
        # if password and password_confirm and password != password_confirm:
        #     raise forms.ValidationError('Password with confirm password must be equal')


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    name = forms.CharField(required=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'category','picture']
