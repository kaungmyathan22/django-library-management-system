from django.contrib import admin
from .models import Book, Author, Category, Shelf
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'amount', 'price', 'available','shelf')
    
    search_fields = ('name', 'author', 'category', 'amount', 'price', 'slug', 'available', 'description', 'image', )
    
    list_filter = ('author', 'category', 'available')    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','born', 'died',)
    
    search_fields = ('first_name', 'last_name',
                     'slug', 'born', 'died', 'image', )

    list_filter = ('first_name', 'last_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug']

    search_fields = ['name']
    

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):

    list_display = ['name',]

    search_fields = ['name']
