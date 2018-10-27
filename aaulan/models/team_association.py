from django.db import models
from django.contrib import admin
from rest_framework import serializers


class TeamAssociation(models.Model):
    class Meta:
        verbose_name = 'Team association'
        unique_together = ('team', 'user')

    is_leader = models.BooleanField(verbose_name='Is team leader')
    user = models.ForeignKey(
        to='Attendance',
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        to='Team',
        on_delete=models.CASCADE,
    )

    def get_event(self):
        return self.team.event
    get_event.short_description = 'Event'

    def __str__(self):
        return self.user.get_user_name()


class TeamAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamAssociation
        fields = ('is_leader', 'user')
        depth = 1


class TeamAssociationAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'is_leader', 'get_event')
    list_filter = ('is_leader', 'team', 'team__event')


admin.site.register(TeamAssociation, TeamAssociationAdmin)
