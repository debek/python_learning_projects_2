from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# To poniżej było na szybko przykładowe
# def home(requests):
#     return HttpResponse("Witaj na mojej stronie zbudowanej za pomocą widoku.")

def home(requests):
    # Poniżej to do testowania strony czyli debugtools
    context = {'title': "Pierwsza strona", 'dump': requests}
    return render(requests, 'library/index.html', context)

