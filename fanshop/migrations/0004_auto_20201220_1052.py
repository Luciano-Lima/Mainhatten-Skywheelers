# Generated by Django 3.0 on 2020-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanshop', '0003_product_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
