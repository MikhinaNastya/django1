from django import forms
from django.contrib.auth import get_user_model

from blog.models import Post


class PostModelForm(forms.ModelForm):
    # title = forms.CharField()
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')