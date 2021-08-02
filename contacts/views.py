from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.views.generic import FormView
from django.contrib import messages
from .forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = '/'

    def form_valid(self, form):
        mail_subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        try:
            send_mail(
                mail_subject,
                message,
                from_email,
                ['freelanceranarul@gmail.com'],
                fail_silently=True
            )
            messages.success(self.request, 'successfully send your mail.')
        except BadHeaderError:
            error_message = messages.success(self.request, 'Invalid header found.')
            return error_message
        return super(ContactFormView, self).form_valid(form)



