from django import forms

from .models import Contact, Newness


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class NewnessForm(forms.ModelForm):
    class Meta:
        model = Newness
        fields = ['title_en', 'title_ru', 'title_uz', 'content_en', 'content_ru', 'content_uz', 'photo', 'category', 'status']