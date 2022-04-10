from django.db import models
from django.urls import reverse

# Dziedziczymy z models.Model i tam jest __init__ dzięki czemu nie musimy tego robić
class Author(models.Model):
    name = models.CharField(max_length=200)
    #Metoda specjalna w pytohonie. Po odbyptaniu o obiekt zwraca to co zrobimy w returnie
    def __str__(self):
        return self.name

# Dziedziczymy z models.Model i tam jest __init__ dzięki czemu nie musimy tego robić
class Book(models.Model):
    # Definicja naszej tabelki i naszego przyszłego obiektu
    # CharFIeld to stringi dla bazodanowców. Textfield przechowuje dłuższy text
    title = models.CharField(max_length=200)
    description = models.TextField()
    # ForeignKey odwolanie do tabeli z Autorami. Tabele utworzymy wcześniej na górze za pomocą klasy
    # on_delete w przypadku usunięcia autora usuwa kaskodowo wszystko co na jego wskazuje
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    # Doda w obiekcie w admin przycisk "View on Site". Na podstawie Models o tej nazwie funkcji samo to robi
    def get_absolute_url(self):
        return reverse('book', args=(self.id,))

