import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Account


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birthdate',
            'password1',
            'password2',
        ]

        widgets = {
            'birthdate': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Majburiy va ixtiyoriy maydonlar
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['birthdate'].required = False

        # Kelajakdagi sanalarni kalendardan tanlashni cheklash
        self.fields['birthdate'].widget.attrs['max'] = (
            timezone.localdate().isoformat()
        )

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')

        if birthdate:
            today = timezone.localdate()

            if birthdate > today:
                raise ValidationError(
                    "Kelajakdagi sanani tanlash mumkin emas."
                )

            age = (
                today.year - birthdate.year
                - (
                    (today.month, today.day)
                    < (birthdate.month, birthdate.day)
                )
            )

            if age < 18:
                raise ValidationError(
                    "Ro'yxatdan o'tish uchun kamida 18 yoshda "
                    "bo'lishingiz kerak."
                )

        return birthdate

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username:
            return username

        pattern = r"^[a-z0-9_-]{3,15}$"

        if not re.fullmatch(pattern, username):
            raise ValidationError(
                "Username 3-15 ta belgidan iborat bo'lishi kerak. "
                "Faqat kichik harflar, raqamlar, _ va - ishlatiladi."
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        pattern = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

        if not re.fullmatch(pattern, email):
            raise ValidationError("Email noto'g'ri formatda!")

        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if not password:
            return password

        if len(password) < 8:
            raise ValidationError(
                "Parol kamida 8 ta belgidan iborat bo'lishi kerak!"
            )

        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Kamida bitta katta harf bo'lishi kerak!"
            )

        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Kamida bitta kichik harf bo'lishi kerak!"
            )

        if not re.search(r'\d', password):
            raise ValidationError(
                "Kamida bitta raqam bo'lishi kerak!"
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=]', password):
            raise ValidationError(
                "Kamida bitta maxsus belgi bo'lishi kerak!"
            )

        return password