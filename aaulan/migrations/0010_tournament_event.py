# Generated by Django 2.1.2 on 2018-10-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aaulan', '0009_auto_20181027_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aaulan.Event'),
            preserve_default=False,
        ),
    ]