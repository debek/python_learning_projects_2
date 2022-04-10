from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author
from .forms import AddBookForm, BookForm_ModelForm, DeleteBookForm
from django.urls import reverse
from django.contrib import messages


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
    # book = Book.objects.get(id=book_id)
    # To poniżej to jest djangoshorcut i da nam 404 jeśli strona nie istnieje
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = DeleteBookForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["operation"] == "delete":
                book.delete()
                messages.success(request, "Usunięto książkę")
                return HttpResponseRedirect(reverse("home"))
    delete_form = DeleteBookForm()

    return render(request, 'library/book.html', {'book': book, "delete_form": delete_form})

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.book_set.all()
    return render(request, 'library/author.html', {'author': author, 'books': books})

def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        # Sprawdza czy sa sprawdzone wszystkie warunki formularza np. dlugosc ciagu i uzupelnia nam pole clean_data
        if form.is_valid():
            # cleaned_data to jest słownik z formularzy, ktory jest oczyszczony z przedrostków itp. Doczytac...
            author = Author.objects.get(name=form.cleaned_data["author_name"])
            book = Book(
                title=form.cleaned_data["title"],
                author=author,
                description=form.cleaned_data["description"]
            )
            book.save()
            # uzyjemu messages do wyświetlenia, że coś zostąło dodane
            # messages.add_message(request, messages.SUCCESS, "Dodano książkę")
            messages.success(request, "Dodano książkę")

            # print(form.cleaned_data)
            #reverse przechodzi na stronę, którą wygenerowaliśmy
            return HttpResponseRedirect(reverse('book', args=(book.id,)))
            # return HttpResponseRedirect(f"/books/{book.id}")
            # return HttpResponse("Ok, dodaję tę książkę")
    else:
        form = AddBookForm()

    return render(request, 'library/add_book.html', {'form': form})

def add_book_modelform(request):
    if request.method == "POST":
        form = BookForm_ModelForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Dodano książkę")
            # To poznizej dodalismy w models wiec pozbywam sie tego
            # return HttpResponseRedirect(reverse('book', args=(book.id,)))
            return HttpResponseRedirect(book.get_absolute_url())
            # To poznizej dodalismy w models wiec pozbywam sie tego
            # return HttpResponseRedirect(reverse('book', args=(book.id,)))
        return HttpResponseRedirect(book.get_absolute_url())
    else:
        form = BookForm_ModelForm()
    return render(request, 'library/add_book.html', {'form': form})
