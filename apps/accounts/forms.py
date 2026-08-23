from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'birthDate',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your last name',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select your gender',
                }
            ),
            'birthDate': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your birth date',
                    'type': 'date',
                }
            )
        }

        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'gender': _('Gender'),
            'birthDate': _('Birth Date'),
            'password1': _('Password'),
            'password2': _('Confirm password'),
        }

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