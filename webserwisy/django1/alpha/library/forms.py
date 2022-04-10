from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Author

# forms.Form - dzidziczymy z tego co zaimportowalismy, zeby django za nas zrobim inita itp.
class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    # Nie hashujemy tego pomimo ze kolejne rozwiazanie jest lepsze bo robilismy pod to walidacje
    author_name = forms.CharField(max_length=200)
    # To zrobi rozwijaną listę autorów
    # author = forms.ModelChoiceField(Author.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 5}),
        required=False
    )

    # Robimy walidacje. Magiczne metody, które django samo robi na podstawie tego co robiliśmy. Mamy to dzieki is_valid zdefionowanie w views.py
    def clean_author_name(self):
        author_name = self.cleaned_data["author_name"]
        if author_name != "Adam Mickiewicz":
            raise ValidationError("Obsługujemy tylko książki Adama Mickiewicza")
        return author_name

# Robimy django ModelForm
class BookForm_ModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

