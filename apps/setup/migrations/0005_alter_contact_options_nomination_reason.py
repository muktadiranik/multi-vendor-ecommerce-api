# Generated by Django 4.0.8 on 2023-01-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0004_alter_nominationtype_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AddField(
            model_name='nomination',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
