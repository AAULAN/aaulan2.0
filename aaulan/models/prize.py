from django.db import models
from django.contrib import admin


class Prize(models.Model):
    class Meta:
        verbose_name = 'Prize'

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    tournament = models.ForeignKey(
        'Tournament',
        on_delete=models.CASCADE
    )


class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'amount')
    ordering = ['tournament', 'name']


admin.site.register(Prize, PrizeAdmin)
