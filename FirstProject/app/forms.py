from django.contrib.auth.models import UserManager
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class MakeaBet(forms.Form):
    money = forms.DecimalField(max_digits=10, decimal_places=1)

class CreateVisaForm(forms.Form):
    money = forms.IntegerField(max_value=1000)
    card_number = forms.IntegerField()
    card_holders_name = forms.CharField()
    expiration_code = forms.CharField()
    cvv = forms.IntegerField(max_value=999)

class TeamForm(forms.Form):
    Team_name = forms.CharField()
    Team_logo = forms.CharField()
    class Meta:
        model = Team
        fields = ['teamName', 'teamLogo']

class UpdateUser(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    new_password = forms.CharField(widget=forms.PasswordInput())

REASON_CHOICES = [
    ("", "Choose an Option"),
    ("Can not withdraw", "Can not withdraw"),
    ("Can not add money", "Can not add money"),
    ("Can not make a bet", "Can not make a bet"),
]

class MakeComment(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    comment = forms.CharField()
    reason = forms.ChoiceField(choices=REASON_CHOICES, required=False)

class Withdraw(forms.Form):
    IBAN = forms.CharField(max_length=20)
    amount = forms.IntegerField()