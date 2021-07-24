from django import forms
from taggit.forms import TagWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description', 'hashtags', 'status')
        labels = {
            # 'description': '',
            'hashtags': '',
            'status': ''
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'post descriptions'}),
            'hashtags': TagWidget(),
            'status': forms.Select(attrs={'class':'form-control'}),
        }