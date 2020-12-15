# Generated by Django 3.0 on 2020-12-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20201215_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventinfo',
            options={},
        ),
        migrations.RemoveField(
            model_name='eventinfo',
            name='time_and_date',
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='short_description',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
