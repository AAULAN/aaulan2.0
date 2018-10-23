from django.db import models
from django.contrib import admin


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

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class TeamAssociationAdmin(admin.ModelAdmin):
    list = ('user', 'team', 'is_leader')
    list_filter = ('is_leader',)


admin.site.register(TeamAssociation, TeamAssociationAdmin)
