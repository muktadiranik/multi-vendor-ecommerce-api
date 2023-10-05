# Generated by Django 4.0.8 on 2023-01-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_alter_addresstype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contacted_by',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contacted_with',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='rental_booking',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Rental/Booking Number'),
        ),
    ]