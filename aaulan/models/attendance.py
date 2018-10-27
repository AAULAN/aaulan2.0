from django.db import models
from django.contrib import admin
from django.conf import settings
from rest_framework import serializers


class Attendance(models.Model):
    class Meta:
        verbose_name = 'Attendance'
        unique_together = ('user', 'event')

    seat = models.CharField(max_length=10)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE
    )

    def get_user_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    get_user_name.short_description = 'Attendant'

    def __str__(self):
        return '{}; {}'.format(self.get_user_name(), self.event.name)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('seat', 'user', 'event')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('get_user_name',  'event', 'seat')
    list_filter = ('event',)


admin.site.register(Attendance, AttendanceAdmin)
