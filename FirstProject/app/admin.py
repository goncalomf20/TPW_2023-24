from django.contrib import admin
from app.models import Team, Game, Bet, comments, Profile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Bet)
admin.site.register(comments)
admin.site.register(Profile)