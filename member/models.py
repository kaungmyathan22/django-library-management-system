from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

def image_upload_path(instance, filename):

    _, extension = filename.split('.')

    current_time = str(now())

    filename = f'student/{current_time}.{extension}'

    return filename


class Member(models.Model):
    """Model definition for Member."""

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=50)

    slug = models.SlugField(null=True, blank=True)

    email = models.EmailField(max_length=254)

    born = models.DateTimeField()

    roll_no = models.CharField(max_length=10)

    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)

    class Meta:
        """Meta definition for Member."""

        ordering = ('pk',)
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        """Unicode representation of Member."""
        return f'{self.first_name} {self.last_name} '
