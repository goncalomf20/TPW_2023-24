from django.shortcuts import render
from app.models import User, Admin, Team, Game, Bet, comments
# Create your views here.

from app.models import User, Admin, Team, Game, Bet, comments
def index(request):
    ls = Game.objects.all()
    ts = {'games' : ls}
    return render(request, "index.html", ts)