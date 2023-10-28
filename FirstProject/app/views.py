import json
import random
from decimal import Decimal
import time
from django.utils import timezone
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


user_username = "ninguem"

def index(request):
    global user_username

    games = Game.objects.all()
    teams = Team.objects.all()

    if len(teams) % 2 == 0:
        nr_games = len(teams) // 2
    else:
        nr_games = (len(teams) - 1) // 2

    if len(games) >= nr_games:
        games = games[(len(games) - nr_games):]

    if len(games) == 0:
        random_teams = list(teams)
        random.shuffle(random_teams)

        if len(random_teams) % 2 != 0:
            random_teams = random_teams[:-1]

        new_games = []
        for idx in range(0, len(random_teams), 2):
            odd1win = round(random.uniform(1.1, 10.0), 1)  # Generate a random float between 1.0 and 10.0
            odd2win = round(random.uniform(1.1, 10.0), 1)
            oddDraw = round(random.uniform(1.1, 10.0), 1)
            g = Game(team1=random_teams[idx], team2=random_teams[idx + 1], odd1win=odd1win, odd2win=odd2win, oddDraw=oddDraw, game_date=timezone.now())
            g.save()
            new_games.append(g)

        games = new_games

    result = []
    #os jogos vão mudar todos os dias, para teste 1 mins
    if int(timezone.now().timestamp()) - int(games[len(games)-1].game_date.timestamp()) >= 60*60:

        for g in Game.objects.filter(win="waiting"):
            win_probability_team1 = 1 / g.odd1win  # Probability of team1 winning
            win_probability_team2 = 1 / g.odd2win  # Probability of team2 winning
            win_probability_draw = 1 / g.oddDraw  # Probability of a draw

            # Generate a random number between 0 and 1
            random_number = random.uniform(0, 1)

            win_prob = 0
            it = 1
            sum = 0
            arr = [(0,0)]
            while sum <= 1:
                if it == 1:
                    arr.append((arr[-1][0] + win_probability_team1, it))
                    sum += win_probability_team1
                    it = 2
                elif it == 2:
                    arr.append((arr[-1][0] + win_probability_team2, it))
                    sum += win_probability_team2
                    it = 3
                elif it == 3:
                    arr.append((arr[-1][0] + win_probability_draw, it))
                    sum += win_probability_draw
                    it = 1

            for inter in arr:
                if random_number <= inter[0]:
                    if inter[1] == 1:
                        g.win = g.team1.teamName
                    elif inter[1] == 2:
                        g.win = g.team2.teamName
                    elif inter[1] == 3:
                        g.win = "empate"

                    g.save()

                    break

            print(random_number,arr)
            g.save()

        if user_username != "ninguem":

            user = User.objects.get(username=user_username)
            profile = Profile.objects.get(user=user)
            print(profile.money)

            for bet in Bet.objects.filter(user=user, checked=0):

                final_odd = 1
                ganhou = True
                for betted_game in bet.games.all():
                    result.append(betted_game)

                    if betted_game.game.win != betted_game.betted:
                        ganhou = False
                        final_odd = 1
                        bet.checked = 1
                        bet.save()


                    if str(betted_game.game.team1) == str(betted_game.betted):
                        final_odd *= betted_game.game.odd1win
                    elif str(betted_game.game.team2) == str(betted_game.betted):
                        final_odd *= betted_game.game.odd2win
                    elif "empate" == betted_game.betted:
                        final_odd *= betted_game.game.oddDraw

                if ganhou:
                    profit = Decimal(bet.money_invested) * Decimal(final_odd)
                    profile.money += Decimal(profit)
                    profile.save()
                    bet.checked = 2
                    bet.save()



        random_teams = list(teams)
        random.shuffle(random_teams)

        if len(random_teams) % 2 != 0:
            random_teams = random_teams[:-1]

        new_games = []
        for idx in range(0, len(random_teams), 2):
            odd1win = round(random.uniform(1.1, 10.0), 1)  # Generate a random float between 1.0 and 10.0
            odd2win = round(random.uniform(1.1, 10.0), 1)
            oddDraw = round(random.uniform(1.1, 10.0), 1)
            g = Game(team1=random_teams[idx], team2=random_teams[idx + 1], odd1win=odd1win, odd2win=odd2win, oddDraw=oddDraw, game_date=timezone.now())
            g.save()
            new_games.append(g)

        games = new_games

    if request.method == "POST":

        user_username = request.POST.get('user')
        bet = request.POST.get('bet')
        bet_data = json.loads(bet)
        print(user_username, bet_data)

        form = MakeaBet(request.POST)

        if form.is_valid():
            # FAZER UMA BET
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

        return render(request, "index.html", {'games' : games, 'teams' : teams, "form": form, "resultados": result})

def login_user(request):
   global user_username

   if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_username = username
            return redirect('/')
        else:
            messages.success(request, ("There was an error loggin in"))
            return redirect('login')

   else:
        return render(request, "login.html", {})

def logout_user(request):
    global user_username
    logout(request)
    user_username = "ninguem"
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