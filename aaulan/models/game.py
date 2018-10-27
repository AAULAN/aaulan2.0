from django.db import models
from django.contrib import admin


class Game(models.Model):
    class Meta:
        verbose_name = 'Game'

    name = models.CharField(max_length=100)


class GameAdmin(admin.ModelAdmin):
    list = ('name',)


admin.site.register(Game, GameAdmin)
