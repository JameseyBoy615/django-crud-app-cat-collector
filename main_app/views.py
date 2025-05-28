from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
# Import the FeedingForm
from .forms import FeedingForm

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
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat, 'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)
