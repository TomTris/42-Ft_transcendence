# Generated by Django 5.1 on 2024-08-19 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('rank_change1', models.IntegerField(default=0)),
                ('rank_change2', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player1', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_player2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
