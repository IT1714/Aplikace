from django.shortcuts import render

from .models import Developer, Game


def index(request):
    """View function for home page of site."""

    num_game = Game.objects.all().count()

    num_developer = Developer.objects.count()

    context = {
        'num_games': num_game,
        'num_developers': num_developer,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)