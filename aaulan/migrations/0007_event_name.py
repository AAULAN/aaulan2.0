# Generated by Django 2.1.2 on 2018-10-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaulan', '0006_delete_gameadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
