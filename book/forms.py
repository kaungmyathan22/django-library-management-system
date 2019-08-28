from django import forms
from .models import (
    Book,
    Category,
    Shelf,
    Author
)


class BookCreationAddForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ('name', 'author', 'category',
                  'amount', 'price', 'image', 'shelf', )


class CategoryCreationForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = ('name',)


class CategoryUpdateForm(forms.ModelForm):

    name = forms.CharField(max_length=120, label="Category Name", widget=forms.TextInput(
        attrs={'placeholder': 'Enter new category name'}))

    class Meta:

        model = Shelf

        fields = ('name',)


class ShelfCreationForm(forms.ModelForm):

    class Meta:

        model = Shelf

        fields = ('name',)


class ShelfUpdateForm(forms.ModelForm):

    name = forms.CharField(max_length=120, label="Shelf Name", widget=forms.TextInput(
        attrs={'placeholder': 'Enter new shelf name'}))

    class Meta:

        model = Shelf

        fields = ('name', 'active')


class AuthorCreationForm(forms.ModelForm):

    class Meta:

        model = Author

        fields = ('first_name', 'last_name', 'born', 'died', 'image', )
