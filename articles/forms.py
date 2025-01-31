from django import forms
from .models import Comment
from .models import Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter article title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your article...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }