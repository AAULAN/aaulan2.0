from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Team, TeamAdmin)
