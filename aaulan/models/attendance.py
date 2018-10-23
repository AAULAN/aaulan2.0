from django.db import models
from django.contrib import admin
from django.conf import settings


class Attendance(models.Model):
    class Meta:
        verbose_name = 'Attendance'

    seat = models.CharField(max_length=10)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class AttendanceAdmin(admin.ModelAdmin):
    list = ('user__first_name', 'user__last_name', 'seat')
    ordering = ['user__first_name', 'user__last_name']


admin.site.regsiter(Attendance, AttendanceAdmin)
