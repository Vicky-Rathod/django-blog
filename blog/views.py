from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView


class HomeView(View):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
