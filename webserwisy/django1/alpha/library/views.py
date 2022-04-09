from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book, Author

# Create your views here.

# To poniżej było na szybko przykładowe
# def home(requests):
#     return HttpResponse("Witaj na mojej stronie zbudowanej za pomocą widoku.")

def home(requests):
    books = Book.objects.all()

    # Poniżej to do testowania strony czyli debugtools
    context = {'title': "Moja biblioteka",
               'dump': requests,
               'books': books,
               }
    #print(request.path, request.method, request.META, request.headers)
    return render(requests, 'library/index.html', context)

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'library/book.html', {'book': book})
