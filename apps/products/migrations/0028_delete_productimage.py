# Generated by Django 4.0.8 on 2023-02-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
