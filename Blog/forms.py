from django import forms
from .models import Post


class PostForms(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
