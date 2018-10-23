from django.db import models
from django.contrib import admin


class Sponsorship(models.Model):
    class Meta:
        verbose_name = 'Sponsorship deal'

    tier = models.IntegerField()
    amount = models.IntegerField()
    sponsor = models.ForeignKey('Sponsor')
    event = models.ForeignKey('Event')


class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('sponsor__name', 'event', 'tier', 'amount')
    ordering = ['event', 'tier']


admin.site.register(Sponsorship, SponsorshipAdmin)
