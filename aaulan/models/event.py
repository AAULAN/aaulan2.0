from django.db import models
from django.contrib import admin


class Event(models.Model):
    class Meta:
        verbose_name = 'Event'

    start = models.DateField()
    end = models.DateField()


class EventAdmin(admin.ModelAdmin):
    list_display = ('start', 'end')


admin.site.register(Event, EventAdmin)
