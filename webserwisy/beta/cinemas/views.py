from django.shortcuts import render
from .models import Movie, Projection

# Rozwiązanie 1, powiazane z index.html
# highlights = Movie.objects.prefetch_related('projection_set').all()

# Rozwiązanie 2, powiazane z index.html
highlights = Projection.objects.prefetch_related().all()

def home(request):
    context = {
        'highlights': highlights
    }
    return render(request, "cinemas/index.html", context)
