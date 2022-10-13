from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Movies

def movie_list_view(request):
    categories = Category.object.all()
    movies = Movies.objects.all()
    new_movies_list = []
    for movie in movies:
        new_movies_list.extend({
            "name": movie.name,
            "poster": movie.poster
        })
    context = {
        'categories': [category.name.Title() for category in categories],
        'movies': new_movies_list
    }
    return HttpResponse('index.html', context)



def movie_detail_view(request, movie_id):
    categories = Category.objects.all()
    movie = Movies.objects.first() #this is supposed to be dynamic, as in it retrieves using the passed parameter
    context = {
        'categories': [category.name.Title() for category in categories],
        'movie': {
            "name": movie.name,
            "poster": movie.poster
        }
    }
    return render(request, 'detale.html', context)