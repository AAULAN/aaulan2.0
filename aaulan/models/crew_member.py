from django.conf import settings
from django.db import models
from django.contrib import admin


class CrewMember(models.Model):
    class Meta:
        verbose_name = 'Crew member'

    photo = models.ImageField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'user__last_name', 'title')
    ordering = ['user__first_name', 'user__last_name']


admin.site.register(CrewMember, CrewMemberAdmin)
