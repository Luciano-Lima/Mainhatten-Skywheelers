# Generated by Django 3.0 on 2020-12-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('heading', models.CharField(default='', max_length=254)),
                ('short_description', models.TextField(default='')),
                ('time_and_date', models.DateTimeField(blank=True, default='', null=True)),
                ('paragraph1', models.TextField(blank=True, default='', null=True)),
                ('paragraph2', models.TextField(blank=True, default='', null=True)),
                ('paragraph3', models.TextField(blank=True, default='', null=True)),
                ('paragraph4', models.TextField(blank=True, default='', null=True)),
                ('paragraph5', models.TextField(blank=True, default='', null=True)),
                ('paragraph6', models.TextField(blank=True, default='', null=True)),
                ('paragraph7', models.TextField(blank=True, default='', null=True)),
                ('paragraph8', models.TextField(blank=True, default='', null=True)),
                ('paragraph9', models.TextField(blank=True, default='', null=True)),
                ('paragraph10', models.TextField(blank=True, default='', null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
