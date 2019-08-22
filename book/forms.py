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
        
        fields = ('name', 'author', 'category', 'amount', 'price', 'image', 'shelf', )

class CategoryCreationForm(forms.ModelForm):
    
    class Meta:
        
        model = Category
        
        fields = ('name',)


class ShelfCreationForm(forms.ModelForm):

    class Meta:

        model = Shelf

        fields = ('name',)

class AuthorCreationForm(forms.ModelForm):
    
    class Meta:

        model = Author

        fields = ('first_name', 'last_name', 'born', 'died', 'image', )
