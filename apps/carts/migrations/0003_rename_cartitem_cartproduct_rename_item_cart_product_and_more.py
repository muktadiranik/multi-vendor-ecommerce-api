# Generated by Django 4.0.8 on 2023-01-08 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_item_type_product_product_type_and_more'),
        ('carts', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='Cartproduct',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cartproduct',
            old_name='item',
            new_name='product',
        ),
    ]
