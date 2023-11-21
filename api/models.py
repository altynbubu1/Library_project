from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=100)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class LibUser(models.Model):
    name = models.CharField(max_length=100)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    returnedDate = models.DateTimeField(null=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.name} rented by {self.user.name} on {self.rentDate}"

class BookCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
