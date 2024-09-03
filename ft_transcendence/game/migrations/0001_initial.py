# Generated by Django 4.2.15 on 2024-09-03 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('connected', models.BooleanField(default=False)),
                ('is_tournament', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_player2', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('game1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game1', to='game.gamesession')),
                ('game2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game2', to='game.gamesession')),
                ('game3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game3', to='game.gamesession')),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament2', to=settings.AUTH_USER_MODEL)),
                ('player3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament3', to=settings.AUTH_USER_MODEL)),
                ('player4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament4', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
