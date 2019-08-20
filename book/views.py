from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book


class DashboardView(TemplateView):
    
    template_name = 'book/dashboard.html'

class BooksListView(ListView):
    
    model = Book