from django.db import models
from django.contrib import admin


class Participation(models.Model):
    class Meta:
        verbose_name = 'Tournament participation'

    position = models.IntegerField(blank=True)
    team = models.ForeignKey(to='Team')
    tournament = models.ForeignKey(to='Tournament')


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('team', 'tournament', 'position')
    ordering = ['tournament', 'position']


admin.site.register(Participation, ParticipationAdmin)
