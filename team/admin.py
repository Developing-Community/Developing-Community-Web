from django.contrib import admin

from .models import Team, TeamUserRelation

admin.site.register(Team)
admin.site.register(TeamUserRelation)
