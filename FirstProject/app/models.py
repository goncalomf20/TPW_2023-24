from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=70, default="")
    password = models.CharField(max_length=70, default="")
    email = models.EmailField()
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    money = models.IntegerField(max_length=10000)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Admin(models.Model):
    username = models.CharField(max_length=70, default="")
    password = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.username

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

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who placed the bet
    games = models.ManyToManyField(Game, related_name='bets')  # Multiple games associated with the bet
    money_invested = models.DecimalField(max_digits=10, decimal_places=2)  # The amount of money invested in the bet
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp when the bet is placed

    def __str__(self):
        return f"{self.user.username}'s Bet ({self.timestamp})"

class comments(models.Model):
    name = models.CharField(max_length=70, default="")
    email = models.EmailField()
    subject = models.CharField(max_length=100, default="")
    reason = models.CharField(max_length=300, default="")