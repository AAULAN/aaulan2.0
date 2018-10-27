from django.db import models
from django.contrib import admin
from rest_framework import serializers

from .prize import Prize, PrizeSerializer


class Tournament(models.Model):
    class Meta:
        verbose_name = 'Tournament'

    start = models.DateTimeField()
    end = models.DateTimeField()
    type = models.CharField(max_length=100)
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        to='Game',
        on_delete=models.CASCADE
    )

    def get_prizes(self):
        return Prize.objects.find(tournament=self).all()

    def __str__(self):
        return '{}, {}'.format(self.event.name, self.game.name)


class TournamentSerializer(serializers.ModelSerializer):
    prize_set = PrizeSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ('start', 'end', 'type', 'game', 'prize_set', 'pk')
        depth = 1


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('game', 'type', 'start', 'end', 'pk')
    list_filter = ('event', 'game')


admin.site.register(Tournament, TournamentAdmin)
