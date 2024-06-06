from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=250, blank=False)
    register_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=250)
    date_birth = models.DateField(blank=False)
    nationality = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250, blank=False)
    date_publishing = models.DateField(blank=False)
    gender = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
    
class Loan(models.Model):
    loan_date = models.DateField(auto_now=True)
    return_date = models.DateField(blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'Usuario: {self.user.name} | Libro: {self.book.title}'
    