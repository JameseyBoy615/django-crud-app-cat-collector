from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello World! ᓚᘏᗢ</h1>')

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Sarabi', 'lion', 'hunts and sleeps.', 5),
#     Cat('Oliver', 'Orange', 'Was cool with some dogs', 1),
#     Cat('Thomas Omalley', 'Orange Stray', 'felt everybody wanted to be a cat', 3 ),
#     Cat('Simba', 'lion cub', 'peer pressured into eating worms', 2),
# ]

def cat_index(request):
    cats = Cat.objects.all() 
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})