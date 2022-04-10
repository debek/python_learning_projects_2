from django import forms
from django.core.exceptions import ValidationError

# forms.Form - dzidziczymy z tego co zaimportowalismy, zeby django za nas zrobim inita itp.
class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author_name = forms.CharField(max_length=200)
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