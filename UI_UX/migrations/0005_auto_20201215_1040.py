# Generated by Django 3.1.1 on 2020-12-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI_UX', '0004_auto_20201215_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfeed',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
