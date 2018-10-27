from django.db import models
from django.contrib import admin


class Participation(models.Model):
    class Meta:
        verbose_name = 'Tournament participation'

    position = models.IntegerField(blank=True)
    team = models.ForeignKey(
        to='Team',
        on_delete=models.CASCADE
    )
    tournament = models.ForeignKey(
        to='Tournament',
        on_delete=models.CASCADE
    )


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('team', 'tournament', 'position')
    ordering = ['tournament', 'position']


admin.site.register(Participation, ParticipationAdmin)
