import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
            }
        )
    )

    gender = forms.ChoiceField(
        choices=User.Gender.choices,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    birthDate = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            # 'email',
            'gender',
            'birthDate',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email is already registered."
            )

        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }
        )
    )

    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }
        )
    )