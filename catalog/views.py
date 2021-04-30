from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    """View function for home page of site."""

    num_game = Game.objects.all().count()

    num_developer = Developer.objects.count()

    latest_game = Game.objects.last()

    context = {
        'num_games': num_game,
        'num_developers': num_developer,
        'latest_game': latest_game,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class GameListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'game_list.html'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game_detail'
    template_name = 'game_detail.html'