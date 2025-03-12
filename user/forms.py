from django import forms

from user.models import Profile


def validate_picture(file):
    max_size_file = 1024 * 1024 * 10
    if file.size > max_size_file:
        raise ValueError('File too large')


# class ProfileForm(ModelForm):
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_profile_picture(self):
        pic = self.cleaned_data.get('profile_picture')
        validate_picture(pic)
        return pic
