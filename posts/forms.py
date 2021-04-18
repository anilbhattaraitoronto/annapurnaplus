from django import forms
from .models import Blog


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['is_featured', 'title',
                  'summary', 'thumbnail', 'content']
