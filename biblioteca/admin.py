from django.contrib import admin
from .models import Author, Book, Loan, User


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(User)