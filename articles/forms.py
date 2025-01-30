from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 5}),
        }
        labels = {
            'text': 'Your Comment',
        }
        help_texts = {
            'text': 'Write your thoughts here. Be respectful!',
        }

    def save(self, user, *args, **kwargs):
        """
        Save the form and associate the comment with the logged-in user.
        """
        comment = super().save(commit=False)  
        comment.user = user 
        comment.save() 
        return comment
