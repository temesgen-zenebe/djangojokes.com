from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView, 
    ListView, 
    UpdateView
)

from .models import Joke

from django.urls import reverse_lazy

from .forms import JokeForm

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm
    #fields = ['question', 'answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm
    #fields = ['question', 'answer']

