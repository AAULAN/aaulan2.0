from django.db import models
from django.contrib import admin


class Sponsor(models.Model):
    class Meta:
        verbose_name = 'Event sponsor'

    name = models.CharField(max_length=100)
    #logo = models.ImageField()
    tagline = models.CharField(max_length=200)
    link = models.URLField(blank=True)


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Sponsor, SponsorAdmin)
