from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'status')
        labels = {
            'title': '',
            'description': '',
            'status': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }