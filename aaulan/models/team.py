from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'

    name = models.CharField(max_length=255)
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'event', 'pk')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'pk')


admin.site.register(Team, TeamAdmin)
