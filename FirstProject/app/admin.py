from django.contrib import admin
from app.models import User, Admin, Team, Game, Bet, comments
# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Bet)
admin.site.register(comments)