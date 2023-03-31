from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ("",)
        exclude = ['post']
        labels = {
            "user_name": "Your name",
            "user_emial": "Your email",
            "text": "Your comment"
        }
