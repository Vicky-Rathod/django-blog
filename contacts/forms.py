from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)