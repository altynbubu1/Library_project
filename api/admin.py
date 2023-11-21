from django.contrib import admin
from .models import Book, BookCategory, RentBook, LibUser

admin.site.register(Book)
admin.site.register(LibUser)
admin.site.register(RentBook)
admin.site.register(BookCategory)
