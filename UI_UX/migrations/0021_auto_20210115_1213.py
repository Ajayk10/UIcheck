# Generated by Django 3.1.1 on 2021-01-15 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UI_UX', '0020_auto_20210110_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfeed',
            name='user_likes',
            field=models.ManyToManyField(to='UI_UX.Membership'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alreadyLiked', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='UI_UX.postfeed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='UI_UX.membership')),
            ],
        ),
    ]