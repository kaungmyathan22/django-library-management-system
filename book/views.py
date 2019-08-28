from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Book, Author, Category, Shelf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import (
    BookCreationAddForm,
    CategoryCreationForm,
    CategoryUpdateForm,
    ShelfCreationForm,
    ShelfUpdateForm,
    AuthorCreationForm,
)


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'book/dashboard.html'

    def get_context_data(self, *args, **kwargs):

        ctx_data = super().get_context_data(*args, **kwargs)

        ctx_data['book_count'] = Book.objects.count()
        ctx_data['author_count'] = Author.objects.count()
        ctx_data['category_count'] = Category.objects.count()
        ctx_data['category_count'] = Category.objects.count()

        return ctx_data


class BooksListView(LoginRequiredMixin, ListView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_form'] = BookCreationAddForm
        return context


class BookCreateView(LoginRequiredMixin, CreateView):

    template_name = 'book/form.html'

    form_class = BookCreationAddForm

    def get_success_url(self):

        return reverse('book:book-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Add Book"
        context['button_name'] = "Create Book"
        return context


class BookUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'book/form.html'

    queryset = Book.objects.all()

    form_class = BookCreationAddForm

    def get_success_url(self):

        return reverse('book:book-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f"Update {self.object.name}"
        context['button_name'] = "Update Book"
        return context


@login_required
def book_delete_view(request, pk):

    instance = get_object_or_404(Book, pk=pk)

    if request.method == "POST":

        book_name = instance.name

        instance.delete()

        return JsonResponse({
            'message': f'Successfully deleted {book_name}.'
        })

class CategoryListView(LoginRequiredMixin, ListView):

    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_update_form"] = CategoryUpdateForm
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):

    form_class = CategoryCreationForm

    template_name = "book/form.html"

    success_url = reverse_lazy("book:category-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Add Category"
        context['button_name'] = "Create Category"
        return context


@login_required
def category_update_view(request, pk):

    instance = get_object_or_404(Category, pk=pk)

    form = ShelfUpdateForm(request.POST or None, instance=instance)

    if request.method == "POST":

        if form.is_valid():

            obj = form.save()

            updated_obj = {
                'name': obj.name,
                'updated': obj.updated_at.strftime("%B. %d, %Y, %I:%M %p"),
            }

        return JsonResponse(updated_obj)


@login_required
def category_delete_view(request, pk):

    instance = get_object_or_404(Category, pk=pk)

    if request.method == "POST":

        category_name = instance.name

        instance.delete()

        return JsonResponse({
            'message': f'Successfully deleted {category_name}.'
        })


class ShelfListView(LoginRequiredMixin, ListView):

    model = Shelf

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shelf_jquery_update"] = json.dumps(True)
        context["shelf_update_form"] = ShelfUpdateForm
        return context


class ShelfCreateView(LoginRequiredMixin, CreateView):

    form_class = ShelfCreationForm

    template_name = "book/form.html"

    success_url = reverse_lazy("book:shelf-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Add Shelf"
        context['button_name'] = "Create Shelf"
        return context


@login_required
def shelf_update_view(request, pk):

    instance = get_object_or_404(Shelf, pk=pk)

    form = ShelfUpdateForm(request.POST or None, instance=instance)

    if request.method == "POST":

        if form.is_valid():

            obj = form.save()

            updated_obj = {
                'name': obj.name,
                'updated': obj.updated_at.strftime("%B. %d, %Y, %I:%M %p"),
            }

        return JsonResponse(updated_obj)


@login_required
def shelf_delete_view(request, pk):

    instance = get_object_or_404(Shelf, pk=pk)

    if request.method == "POST":

        shelf_name = instance.name

        instance.delete()

        return JsonResponse({
            'message': f'Successfully deleted {shelf_name}.'
        })


class AuthorListView(LoginRequiredMixin, ListView):

    model = Author


class AuthorCreateView(LoginRequiredMixin, CreateView):

    form_class = AuthorCreationForm

    template_name = "book/form.html"

    success_url = reverse_lazy("book:author-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = reverse('book:author-create')
        context['file_upload'] = True
        context['header'] = "Add Author"
        context['button_name'] = "Create Author"
        return context


class AuthorUpdateView(LoginRequiredMixin, UpdateView):

    model = Author

    form_class = AuthorCreationForm

    template_name = "book/form.html"

    success_url = reverse_lazy("book:author-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_upload'] = True
        context['header'] = "Update {} {} Info".format(
            self.object.first_name, self.object.last_name)
        context['button_name'] = "Update Author"
        return context


@login_required
def author_delete_view(request, pk):

    instance = get_object_or_404(Author, pk=pk)

    if request.method == "POST":

        author_name = str(instance)

        instance.delete()

        return JsonResponse({
            'message': f'Successfully deleted {author_name}.'
        })
