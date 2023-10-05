# Generated by Django 4.0.8 on 2023-01-19 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productsize',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsize',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]