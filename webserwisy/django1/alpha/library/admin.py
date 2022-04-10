from django.contrib import admin

from .models import Book, Author

# Dodanie modeli do panelu admina
admin.site.register(Book)
admin.site.register(Author)
