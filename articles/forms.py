from django import forms
from .models import Comment  # Import the Comment model

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Include only the content field in the form
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'comment-input',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }
        labels = {
            'content': '',
        }
