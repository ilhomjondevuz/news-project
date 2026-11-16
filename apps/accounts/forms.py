import re
from datetime import date

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Account


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'birthdate', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['birthdate'].required = False
        self.fields['password1'].required = True
        self.fields['password2'].required = True

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')

        if birthdate:
            today = date.today()

            age = (
                    today.year - birthdate.year
                    - ((today.month, today.day) < (birthdate.month, birthdate.day))
            )

            if age < 18:
                raise ValidationError("Ro'yxatdan o'tish uchun kamida 18 yoshda bo'lishingiz kerak.")

        return birthdate

    def clean_username(self):
        username = self.cleaned_data.get('username')
        USERNAME_PATTERN = r"^[a-z0-9_-]{3,15}$"
        if not re.fullmatch(USERNAME_PATTERN, username):
            raise ValidationError(
                "Username 3-15 ta belgidan iborat bo'lishi kerak. "
                "Faqat kichik harflar, raqamlar, _ va - ishlatiladi."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        EMAIL_PATTERN = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        if not re.fullmatch(EMAIL_PATTERN, email):
            raise ValidationError("Email noto'g'ri formatda!")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if not password:
            raise ValidationError("Parol kiritilishi shart!")

        if len(password) < 8:
            raise ValidationError("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")

        if not re.search(r'[A-Z]', password):
            raise ValidationError("Kamida bitta katta harf bo'lishi kerak!")

        if not re.search(r'[a-z]', password):
            raise ValidationError("Kamida bitta kichik harf bo'lishi kerak!")

        if not re.search(r'\d', password):
            raise ValidationError("Kamida bitta raqam bo'lishi kerak!")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=]', password):
            raise ValidationError("Kamida bitta maxsus belgi bo'lishi kerak!")

        return password

    def clean(self):
        clean_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Parollar mos emas')
        return clean_data