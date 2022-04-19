from django.shortcuts import render
from .models import Movie


highlights = Movie.objects.prefetch_related('projection_set').all()[:]

def home(request):
    context = {
        'highlights': highlights
    }
    return render(request, "cinemas/index.html", context)
