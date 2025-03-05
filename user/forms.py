from django import forms

from user.models import Profile


# class ProfileForm(ModelForm):
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','location']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'bio' : forms.TextInput(attrs={'class':'form-control'}),
            'location':  forms.TextInput(attrs={'class':'form-control'}),
        }

