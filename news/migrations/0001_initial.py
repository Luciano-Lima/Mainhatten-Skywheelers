# Generated by Django 3.0 on 2020-07-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsHeadlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('heading', models.CharField(default='', max_length=254)),
                ('time_and_date_published', models.DateTimeField(default='')),
            ],
        ),
    ]
