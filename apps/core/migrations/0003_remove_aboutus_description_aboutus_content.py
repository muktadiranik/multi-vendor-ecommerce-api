# Generated by Django 4.0.8 on 2023-01-23 09:01

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_aboutus_options_alter_privacypolicy_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='description',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='content',
            field=django_quill.fields.QuillField(),
            preserve_default=False,
        ),
    ]