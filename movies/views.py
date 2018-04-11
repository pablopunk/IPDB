from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def home(request):
    movies = Movie.objects.all().order_by('-release_date')[:5]
    ctx = { 'latest_movies': movies }

    return render(request, 'home.html', ctx)

def movie_detail(request, pk):
    movies = Movie.objects.filter(pk=pk).select_related('category')
    if len(movies) == 0:
        return render(request, '404.html', status=404)
    return render(request, 'movie_detail.html', { 'movie': movies[0]})