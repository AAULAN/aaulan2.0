from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Event(models.Model):
    class Meta:
        verbose_name = 'Event'

    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'start', 'end', 'pk')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')


admin.site.register(Event, EventAdmin)
