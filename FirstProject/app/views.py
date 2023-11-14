import json
import random
from decimal import Decimal
import time

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from app.models import Team, Game, Bet, comments, Profile, Game_betted, PaymentMethod
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth import login
from django.contrib import messages
from .forms import CreateUserForm, MakeaBet, CreateVisaForm, TeamForm, UpdateUser, MakeComment, Withdraw
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect


user_username = "ninguem"

def index(request):
    global user_username

    games = Game.objects.all()
    teams = Team.objects.all()
    print(teams)
    if not teams:
        form = MakeaBet(request.POST)
        result = []
        comment_form = MakeComment(request.POST)
        return render(request, "index.html", {'games' : games, 'teams' : teams, "form": form, "resultados": result, "comment_form":comment_form})

    #pelas equipas saber o nr de jogos possiveis
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
            odd1win = round(random.uniform(1.1, 5.0), 1)
            odd2win = round(random.uniform(1.1, 10.0), 1)
            oddDraw = round(random.uniform(1.1, 5.0), 1)
            g = Game(team1=random_teams[idx], team2=random_teams[idx + 1], odd1win=odd1win, odd2win=odd2win, oddDraw=oddDraw, game_date=timezone.now())
            g.save()
            new_games.append(g)

        games = new_games

    result = []
    #os jogos vão mudar todos os dias, para teste 1 mins
    if int(timezone.now().timestamp()) - int(games[len(games)-1].game_date.timestamp()) >= 30:

        for g in Game.objects.filter(win="waiting"):
            win_probability_team1 = 1 / g.odd1win
            win_probability_team2 = 1 / g.odd2win
            win_probability_draw = 1 / g.oddDraw

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

                result.append(bet)

        random_teams = list(teams)
        random.shuffle(random_teams)

        if len(random_teams) % 2 != 0:
            random_teams = random_teams[:-1]

        new_games = []
        for idx in range(0, len(random_teams), 2):
            odd1win = round(random.uniform(1.1, 10.0), 1)
            odd2win = round(random.uniform(1.1, 10.0), 1)
            oddDraw = round(random.uniform(1.1, 10.0), 1)
            g = Game(team1=random_teams[idx], team2=random_teams[idx + 1], odd1win=odd1win, odd2win=odd2win, oddDraw=oddDraw, game_date=timezone.now())
            g.save()
            new_games.append(g)

        games = new_games

    if request.method == "POST":
        comment_form = MakeComment(request.POST)
        if comment_form.is_valid():
            print(comment_form.cleaned_data)
            name = comment_form.cleaned_data['name']
            email = comment_form.cleaned_data['email']
            subject = comment_form.cleaned_data['subject']
            comment = comment_form.cleaned_data['comment']
            reason = comment_form.cleaned_data['reason']

            full_comment = comments(name=name, email=email, subject=subject, comment=comment, reason=reason)
            full_comment.save()
            return redirect('/')

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
        comment_form = MakeComment()

        return render(request, "index.html", {'games' : games, 'teams' : teams, "form": form, "resultados": result, "comment_form":comment_form})

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

            if user.is_staff:
                return redirect('admin_page')
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

def usrdetails(request):
    user = request.user
    context = {
        'user': user,

    }

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            login(request, user)
            messages.success(request, ("Update Sucessful"))
            return redirect('/')
    else:
        return render(request,"usrdetails.html" , context)
def admin_page(request):

    games = Game.objects.all().order_by("-game_date")
    teams = Team.objects.all()
    profiles = Profile.objects.all()
    betted_games = Game_betted.objects.all()
    bets = Bet.objects.all()
    team_form = TeamForm()
    ts = {"games": games, "teams": teams, "profiles" : profiles, "betted_games" : betted_games, "bets" : bets, "team_form": team_form}
    return render(request, "admin_page.html", ts)

def delete_team(request, team_name):
    try:
        team = Team.objects.get(teamName=team_name)
        team.delete()
    except Team.DoesNotExist:
        pass
    return redirect('admin_page')

def delete_game(request, game_identifier):
    try:
        game = Game.objects.get(game_date=game_identifier)

        game.delete()
    except Game.DoesNotExist:
        pass

    return redirect('admin_page')

def search_games(request):
    teams = Team.objects.all()
    profiles = Profile.objects.all()
    betted_games = Game_betted.objects.all()
    bets = Bet.objects.all()

    search_query = request.GET.get('search_query', '')

    games = Game.objects.filter(
        win__icontains=search_query,
    ) | Game.objects.filter(
        team1__teamName__icontains=search_query,
    ) | Game.objects.filter(
        team2__teamName__icontains=search_query,
    )
    games = games.order_by("-game_date")
    ts = {"games": games, "teams": teams, "profiles": profiles, "betted_games": betted_games, "bets": bets}
    return render(request, 'admin_page.html', ts)

def update_game_odds(request, game_id):
    if request.method == 'POST':
        try:
            game = Game.objects.get(id=game_id)
            game.odd1win = request.POST['odd1win']
            game.oddDraw = request.POST['oddDraw']
            game.odd2win = request.POST['odd2win']
            game.save()
        except Game.DoesNotExist:
            pass

    return redirect('admin_page')


def add_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            team_name = team_form.cleaned_data['Team_name']
            team_logo = team_form.cleaned_data['Team_logo']
            image = team_form.cleaned_data['image']
            team = Team(teamName=team_name, teamLogo=team_logo, image=image)
            team.save()

    return redirect('admin_page')

@csrf_protect
def addadmin(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            hashed_password = make_password(password)

            user = User(username=username, password=hashed_password, email=email, first_name=firstname, last_name=lastname)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            messages.success(request, ("Registration Sucessful"))

    else:
        form = CreateUserForm()

    return render(request, "addadmin.html", {"form": form})

def managebets(request):
    betted_games = Game_betted.objects.all()
    dic = {}
    for bet in betted_games:

        bol = False
        for info in dic.keys():
            if info.game == bet.game and info.betted == bet.betted:
                bol = True
                bet_rep = info

        if bol:
            dic[bet_rep] += 1
        else:
            dic[bet] = 1

    print(dic)

    return render(request, "managebets.html", {'betted_games':dic})

def manageusers(request):
    admin_users = User.objects.filter(is_staff=True)
    casual_users = User.objects.filter(is_staff=False)

    dic = {}

    for user in casual_users:
        dic[user.username] = Bet.objects.filter(user=user)
    print(dic)
    ts = {'admin_users': admin_users, 'casual_users':casual_users, 'user_bets': dic}
    return render(request, 'manageusers.html', ts)

def user_bets(request):
    user = request.user
    user_bets = Bet.objects.filter(user=user)  # Replace with the actual filtering logic
    return render(request, 'user_bets.html', {'user_bets': user_bets})

def delete_user(request, username):
    try:
        user = User.objects.get(username=username)
        user.delete()
    except User.DoesNotExist:
        pass

    return redirect('manageusers')

def usrdetails(request):
    user = request.user
    context = {'user': user , "form": UpdateUser()}
    if request.method == "POST":
        form = UpdateUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.password = make_password(form.cleaned_data['new_password'])
            user.save()

            messages.success(request, "Update Successful")
            return redirect('/')
        else:
            messages.error(request, "Update Failed. Please correct the errors.")

    return render(request, "usrdetails.html", context)

def update_admin(request):
    user = request.user
    context = {'user': user , "form": UpdateUser()}
    if request.method == "POST":
        form = UpdateUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.password = make_password(form.cleaned_data['new_password'])
            user.save()

            messages.success(request, "Update Successful")
            return redirect('/')
        else:
            messages.error(request, "Update Failed. Please correct the errors.")

    return render(request, "update_admin.html", context)

def withdraw(request):
    if request.method == "POST":
        withdraw_form = Withdraw(request.POST)
        print(withdraw_form.is_valid())
        if withdraw_form.is_valid():
            print(withdraw_form.cleaned_data)
            iban = withdraw_form.cleaned_data['IBAN']
            # Get the user (assuming the user is logged in)
            user = request.user
            user_profile = user.profile

            withdrawal_amount = withdraw_form.cleaned_data['amount']
            if user_profile.money >= withdrawal_amount:
                user_profile.money -= withdrawal_amount
                user_profile.save()
                messages.success(request, "Withdrawal successful!")
            else:
                messages.error(request, "Insufficient funds for withdrawal.")
                return redirect('withdraw')

            return redirect('/')
        else:
            messages.error(request, "Invalid form data. Please check your input.")
    else:
        withdraw_form = Withdraw()

    return render(request, "withdraw.html", {"withdraw_form": withdraw_form})


def viewcomments(request):
    comment = comments.objects.all()
    return render(request, 'viewcomments.html',{'comments': comment})

def delete_comment(request, id):
    try:
        comment = comments.objects.get(id=id)
        comment.delete()
    except comment.DoesNotExist:
        pass

    return redirect('viewcomments')