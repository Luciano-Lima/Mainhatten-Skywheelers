# Generated by Django 3.0 on 2020-12-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201215_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='end_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='eventinfo',
            name='start_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
