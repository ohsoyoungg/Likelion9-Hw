from django import forms
from .models import Blog

class BlogForm(froms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer','body','image']