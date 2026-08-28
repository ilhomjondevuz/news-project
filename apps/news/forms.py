from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Contact, Newness, Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class NewnessForm(forms.ModelForm):
    class Meta:
        model = Newness
        fields = ['title_en', 'title_ru', 'title_uz', 'content_en', 'content_ru', 'content_uz', 'photo', 'category', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control','cols': 80, 'rows': 5, 'placeholder': _('Write your comment...')}),
        }