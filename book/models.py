from django.db import models
from django.utils.timezone import datetime


def image_upload_path(instance, filename):

    _, extension = filename.split('.')

    current_time = str(datetime.now())

    filename = f'{current_time}.{extension}'

    return filename


class CreatedUpdatedMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class Shelf(CreatedUpdatedMixin):
    """Model definition for Shelf."""

    name = models.CharField(max_length=100, verbose_name="Shelf name")

    active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Category."""
        ordering = ('-created_at', '-updated_at')
        verbose_name = 'Shelf'
        verbose_name_plural = 'Shelfs'

    def __str__(self):
        return self.name


class Category(CreatedUpdatedMixin):
    """Model definition for Category."""

    name = models.CharField(max_length=50)

    slug = models.SlugField(null=True, blank=True)

    class Meta:
        """Meta definition for Category."""
        ordering = ('-created_at', '-updated_at')
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Book(CreatedUpdatedMixin):
    """Model definition for Book."""

    name = models.CharField(max_length=50)

    author = models.ManyToManyField(to="Author", related_name='books')

    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True, related_name='books')

    amount = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Unit Price")

    slug = models.SlugField(null=True, blank=True)

    available = models.BooleanField(default=True)

    description = models.TextField()

    image = models.ImageField(
        upload_to=image_upload_path, null=True, blank=True)

    shelf = models.ForeignKey(
        to="Shelf", on_delete=models.SET_NULL, null=True, blank=True, related_name='books')

    class Meta:
        """Meta definition for Book."""

        ordering = ('-created_at', '-updated_at')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return self.name


class Author(CreatedUpdatedMixin):
    """Model definition for Author."""

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    slug = models.SlugField(null=True, blank=True)

    born = models.DateTimeField()

    died = models.DateTimeField(null=True, blank=True)

    image = models.ImageField(
        upload_to=image_upload_path, null=True, blank=True)

    class Meta:
        """Meta definition for Author."""

        ordering = ('-created_at', '-updated_at')
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return f'{self.first_name} {self.last_name}'
