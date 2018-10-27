from django.db import models
from django.contrib import admin


class Game(models.Model):
    class Meta:
        verbose_name = 'Game'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Game, GameAdmin)
