from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Sponsorship(models.Model):
    class Meta:
        verbose_name = 'Sponsorship deal'

    tier = models.IntegerField()
    amount = models.IntegerField()
    sponsor = models.ForeignKey(
        to='Sponsor',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE
    )

    def get_sponsor_name(self):
        return self.sponsor.name


class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ('tier', 'amount', 'sponsor')


class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('get_sponsor_name', 'event', 'tier', 'amount')
    ordering = ['event', 'tier']


admin.site.register(Sponsorship, SponsorshipAdmin)
