
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import UserManager
# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return str(self.user)


class Team(models.Model):
    teamName = models.CharField(max_length=70, default="")
    teamLogo = models.CharField(max_length=70, default="")
    def __str__(self):
        return self.teamName

class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_bets', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_bets', on_delete=models.CASCADE)
    odd1win = models.FloatField(max_length=20)
    odd2win = models.FloatField(max_length=20)
    oddDraw = models.FloatField(max_length=20, default=2)
    win = models.CharField(max_length=70, default="waiting")
    game_date = models.DateTimeField(default=timezone.now)

    def get_game_identifier(self):
        return f"Game between {self.team1} and {self.team2}, win: {self.win}, on {self.game_date}"

    def __str__(self):
        return f"Game between {self.team1} and {self.team2}, win: {self.win}, on {self.game_date}"

class Game_betted(models.Model):
    game = models.ForeignKey(Game, related_name='game', on_delete=models.CASCADE)
    betted = models.CharField(max_length=70, default="")

    def __str__(self):
        return f"{self.betted}"

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who placed the bet
    games = models.ManyToManyField(Game_betted, related_name='bets')  # Multiple games associated with the bet
    money_invested = models.DecimalField(max_digits=10, decimal_places=2)  # The amount of money invested in the bet
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp when the bet is placed
    checked = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Bet ({self.timestamp})"

class comments(models.Model):
    name = models.CharField(max_length=70, default="")
    email = models.EmailField()
    subject = models.CharField(max_length=100, default="")
    reason = models.CharField(max_length=300, default="")


class PaymentMethod(models.Model):
    user = models.ForeignKey(Profile, related_name='payment_methods', on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_holders_name = models.CharField(max_length=100)

    def __str__(self):
        return self.card_number,self.card_holders_name,self.user.user