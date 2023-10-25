from django.contrib.auth.models import UserManager
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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