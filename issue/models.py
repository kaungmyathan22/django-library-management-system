from django.db import models
from member.models import Member
from book.models import Book

class Issue(models.Model):

    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)

    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    date = models.DateTimeField()

    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.member} borrow {self.book}'
    