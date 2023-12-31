# Generated by Django 4.0.8 on 2023-02-02 07:11

import apps.shops.models
import apps.utilities.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0010_alter_shop_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_cover',
            field=models.ImageField(blank=True, null=True, upload_to=apps.shops.models.shop_cover_directory_path, validators=[apps.utilities.validators.validate_shop_cover_size]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.shops.models.shop_directory_path, validators=[apps.utilities.validators.validate_shop_image_size]),
        ),
    ]
