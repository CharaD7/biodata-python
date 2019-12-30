from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from .models import Biodata
from django.core.exceptions import ValidationError


# Creating an object to interact with bootstrap datepicker
class DateInput(forms.DateInput):
    input_type = 'date'


# Creating a model to handle our forms
class BiodataForm(forms.ModelForm):

    class Meta:
        model = Biodata

        fields = [
            'firstname',
            'lastname',
            'age',
            'date_of_birth',
            'date_of_employment',
            'salary',
            'supervisors',
            ]
        widgets = {
            'date_of_birth': DateInput(),
            'date_of_employment': DateInput(),
            }
        exclude = ('supervisors',)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(
        label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user
