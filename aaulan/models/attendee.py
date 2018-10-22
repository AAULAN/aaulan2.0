from django.db import models
from django.conf import settings
from django.contrib import admin

from .team import Team


class Attendee(models.Model):
    class Meta():
        verbose_name = 'Attendee'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team, blank=True)
    ticket = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Attendee, AttendeeAdmin)