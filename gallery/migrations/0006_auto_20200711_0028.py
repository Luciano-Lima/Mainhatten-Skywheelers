# Generated by Django 3.0 on 2020-07-11 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200711_0002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='firstGalleryPage',
            new_name='firstGalleryPictures',
        ),
        migrations.RenameModel(
            old_name='secondGalleryPage',
            new_name='secondGalleryPictures',
        ),
        migrations.RenameModel(
            old_name='thirdGalleryPage',
            new_name='thirdGalleryPictures',
        ),
    ]
