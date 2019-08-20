from django.urls import path
from .views import DashboardView, BooksListView

app_name='book'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('book/list/', BooksListView.as_view(), name='book-list'),
]