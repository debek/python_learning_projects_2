from django.contrib import admin
from django.urls import path
# To poniżej zaimportowaliśmy. Służy między innymi do szybkiego wpisania tekstu na WWW
from django.http import HttpResponse
import library.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # To poniżej pozwala bezpośrednio odpalić jakiś tekst na WWW. To takie tymczasowe rozwiązanie.
    # path('', lambda request: HttpResponse("Witaj na mojej stronie!"))

    # To poniżej importuje z pliku views.py funkcje
    path('', library.views.home, name="home"),
    path('books/add', library.views.add_book, name="add book"),
    path('books/add_modelform', library.views.add_book_modelform, name="add book with modelform"),
    path('books/<int:book_id>', library.views.book, name="book"),
    path('author/<int:author_id>', library.views.author, name="author"),
]
