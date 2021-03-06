from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from . import forms
# Create your views here.
class SignUp(TemplateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
