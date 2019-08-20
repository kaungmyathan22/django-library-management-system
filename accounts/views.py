from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms
# Create your views here.

class HomePageTemplateView(TemplateView):

    template_name = "accounts/home.html"

class SignUpView(CreateView):

    template_name = 'registration/signup.html'

    form_class = forms.SignUpForm

    success_url = reverse_lazy("login")
