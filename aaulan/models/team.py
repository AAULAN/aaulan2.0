from django.db import models
from django.contrib import admin


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'

    name = models.CharField(max_length=255)
    leader = models.ForeignKey('Attendance', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Team, TeamAdmin)
