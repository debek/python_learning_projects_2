"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('', library.views.home),
    path('books/<int:book_id>', library.views.book)

]
