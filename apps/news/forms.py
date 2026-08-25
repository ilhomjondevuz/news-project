from django import forms

from .models import Contact, Newness


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class NewnessForm(forms.ModelForm):
    class Meta:
        model = Newness
        fields = ['title', 'content', 'photo', 'category', 'status']