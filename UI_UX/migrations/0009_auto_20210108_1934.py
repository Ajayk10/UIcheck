# Generated by Django 3.1.1 on 2021-01-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UI_UX', '0008_auto_20210108_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='joined',
            new_name='joined_on',
        ),
    ]