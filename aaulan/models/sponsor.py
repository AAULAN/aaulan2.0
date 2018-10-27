from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Sponsor(models.Model):
    class Meta:
        verbose_name = 'Event sponsor'

    name = models.CharField(max_length=100)
    #logo = models.ImageField()
    tagline = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'tagline', 'link')


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Sponsor, SponsorAdmin)
