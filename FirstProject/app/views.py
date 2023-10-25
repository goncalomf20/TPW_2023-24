import json

from app.models import Team, Game, Bet, comments, Profile, Game_betted, PaymentMethod
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from .forms import CreateUserForm, MakeaBet, CreateVisaForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    games = Game.objects.all()
    teams = Team.objects.all()
    ts = {'games' : games, 'teams' : teams}

    if request.method == "POST":

        user_username = request.POST.get('user')
        bet = request.POST.get('bet')
        bet_data = json.loads(bet)
        print(user_username, bet_data)

        form = MakeaBet(request.POST)

        if form.is_valid():
            money = form.cleaned_data['money']
            user = User.objects.get(username=user_username)
            profile = Profile.objects.get(user=user)
            profile.money -= money
            profile.save()

            user_bet = Bet(user=user, money_invested=money)
            user_bet.save()

            for game_ in bet_data.keys():

                teams = game_.split("   ")
                print(teams)
                team1 = Team.objects.get(teamName__iexact=teams[0])
                team2 = Team.objects.get(teamName__iexact=teams[2])
                print(team1, team2)
                game = Game()
                for one_game in games:
                    if one_game.team1 == team1 and one_game.team2 == team2:
                        game = one_game
                        break

                print(game)

                betted_game = Game_betted(game=game, betted=teams[3][1:-1])
                betted_game.save()
                user_bet.games.add(betted_game)

            return redirect('/')
    else:
        form = MakeaBet()

    return render(request, "index.html", {'games' : games, 'teams' : teams, "form": form})

def login_user(request):
   if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There was an error loggin in"))
            return redirect('login')

   else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    return redirect('/')

def addmoney(request):
    return render(request,"addmoney.html",{})

@csrf_protect
def register_user(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            prof= Profile()
            prof.user = user
            prof.money = 0
            prof.save()

            login(request, user)
            messages.success(request, ("Registration Sucessful"))
            return redirect('/')
    else:
        form = CreateUserForm()


    return render(request, "register.html", {"form": form})

@csrf_protect
def addmoney(request):
    if request.method == "POST":
        visa_form = CreateVisaForm(request.POST)
        if visa_form.is_valid():
            card_number = visa_form.cleaned_data['card_number']
            card_holders_name = visa_form.cleaned_data['card_holders_name']
            money = visa_form.cleaned_data['money']
            # Get the user for whom the card is being added (assuming the user is logged in)
            user = request.user
            user.profile.money += money
            user.profile.save()


            # Save the card information to the database
            credit_card = PaymentMethod(
                    user=user.profile,
                    card_number=card_number,
                    card_holders_name=card_holders_name,
                )
            credit_card.save()
            messages.success(request, "Money added successfully!")
            return redirect('/')
        else:
            messages.error(request, "Invalid form data. Please check your input.")
    else:
        visa_form = CreateVisaForm()

    return render(request, "addmoney.html", {"visa_form": visa_form})