# Generated by Django 4.0.8 on 2023-01-30 12:22

import apps.shops.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_shop_closing_time_shop_openening_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_cover',
            field=models.ImageField(blank=True, null=True, upload_to=apps.shops.models.shop_directory_path),
        ),
    ]