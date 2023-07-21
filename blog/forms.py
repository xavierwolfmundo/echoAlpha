from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post'].widget = forms.HiddenInput()
