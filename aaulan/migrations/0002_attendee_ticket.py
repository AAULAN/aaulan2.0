# Generated by Django 2.1.2 on 2018-10-06 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaulan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='ticket',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]