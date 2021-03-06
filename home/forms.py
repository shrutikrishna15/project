

from django import forms
from home.models import Post,Comment


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)
