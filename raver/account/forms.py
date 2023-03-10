"""
This is a login form to allow users to login to the site.
"""

from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return clean_data['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already in use.")
        return data


# Edit user form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.filter(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return data


# Edit profile form
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')