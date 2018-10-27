from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Prize(models.Model):
    class Meta:
        verbose_name = 'Prize'

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    tournament = models.ForeignKey(
        'Tournament',
        on_delete=models.CASCADE
    )


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ('name', 'amount')


class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'amount')
    ordering = ['tournament', 'name']
    list_filter = ('tournament__event', 'tournament')


admin.site.register(Prize, PrizeAdmin)
