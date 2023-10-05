# Generated by Django 4.0.8 on 2023-01-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_item_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='padi_at',
        ),
        migrations.AddField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
