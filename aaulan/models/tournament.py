from django.db import models
from django.contrib import admin

from . import Prize


class Tournament(models.Model):
    class Meta:
        verbose_name = 'Tournament'

    start = models.DateTimeField()
    end = models.DateTimeField()
    type = models.CharField(max_length=100)

    def get_prizes(self):
        return Prize.objects.find(tournament=self).all()


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'type')


admin.site.register(Tournament, TournamentAdmin)
