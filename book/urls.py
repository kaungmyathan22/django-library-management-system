from django.urls import path
from .views import (
    DashboardView,
    
    BooksListView,
    BookCreateView,
    BookUpdateView,
    book_delete_view,

    CategoryListView,
    CategoryCreateView,
    category_update_view,
    category_delete_view,
    
    ShelfListView,
    ShelfCreateView,
    shelf_delete_view,
    shelf_update_view,
    
    AuthorCreateView,
    AuthorListView,
    AuthorUpdateView,
    author_delete_view,
)

app_name = 'book'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    path('book/list/', BooksListView.as_view(), name='book-list'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/update/<slug:slug>/', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', book_delete_view, name='book-delete'),
    
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', category_update_view, name='category-update'),
    path('category/delete/<int:pk>/', category_delete_view, name='category-delete'),
    
    path('shelf/list/', ShelfListView.as_view(), name='shelf-list'),
    path('shelf/create/', ShelfCreateView.as_view(), name='shelf-create'),
    path('shelf/update/<int:pk>/', shelf_update_view, name='shelf-update'),
    path('shelf/delete/<int:pk>/', shelf_delete_view, name='shelf-delete'),
    
    path('author/list/', AuthorListView.as_view(), name='author-list'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/update/<int:pk>/',
         AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', author_delete_view, name='author-delete'),
]
