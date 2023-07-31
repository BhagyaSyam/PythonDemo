# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .forms import MovieForm


# Create your views here.


def index(request):
    movie = movies.objects.all()
    context = {
        'movies_list': movie
    }

    return render(request, 'index.html', context)


def detail(request, movies_id):
    movie = movies.objects.get(id=movies_id)
    return render(request, 'detail.html', {'movies': movie})


def add_movies(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie = movies(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movies': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
