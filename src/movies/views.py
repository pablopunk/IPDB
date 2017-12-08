from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def home(request):
    movies = Movie.objects.all().order_by('-release_date')[:5]
    ctx = { 'latest_movies': movies }

    return render(request, 'home.html', ctx)
