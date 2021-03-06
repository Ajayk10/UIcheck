# Generated by Django 3.1.1 on 2021-01-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI_UX', '0005_auto_20201215_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
