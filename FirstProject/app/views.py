
from app.models import Team, Game, Bet, comments
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    games = Game.objects.all()
    teams = Team.objects.all()
    ts = {'games' : games, 'teams' : teams}
    return render(request, "index.html", ts)

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
            username = form.cleaned_data['. ']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Sucessful"))
            return redirect('/')
    else:
        form = CreateUserForm()


    return render(request, "register.html", {"form": form})