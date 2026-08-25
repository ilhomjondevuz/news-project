from django import forms

from .models import Contact, Newness, Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class NewnessForm(forms.ModelForm):
    class Meta:
        model = Newness
        fields = ['title', 'content', 'photo', 'category', 'status']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Write your comment...',
                }
            )
        }