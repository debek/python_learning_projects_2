from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# To poniżej było na szybko przykładowe
# def home(requests):
#     return HttpResponse("Witaj na mojej stronie zbudowanej za pomocą widoku.")

def home(requests):
    print(requests)
    # To fajne do testowania co nie dziala
    # context = {'title': "Pierwsza strona", 'dump': requests}
    context = {'title': "Pierwsza strona", 'dump': requests}
    return render(requests, 'library/index.html', context)

