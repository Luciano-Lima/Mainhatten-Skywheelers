# Generated by Django 3.0 on 2020-12-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_firstgallerypictures_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondgallerypictures',
            name='friendly_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='thirdgallerypictures',
            name='friendly_name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
