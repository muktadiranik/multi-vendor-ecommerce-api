# Generated by Django 4.0.8 on 2023-02-07 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
