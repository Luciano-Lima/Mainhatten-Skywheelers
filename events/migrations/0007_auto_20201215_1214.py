# Generated by Django 3.0 on 2020-12-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20201215_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='end_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='paragraph1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='short_description',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='start_date',
            field=models.DateTimeField(default=None),
        ),
    ]
