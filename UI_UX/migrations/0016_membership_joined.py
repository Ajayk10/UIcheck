# Generated by Django 3.1.1 on 2021-01-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI_UX', '0015_auto_20210109_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='joined',
            field=models.DateField(null=True),
        ),
    ]
