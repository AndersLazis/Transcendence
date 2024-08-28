# Generated by Django 5.0.6 on 2024-08-21 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('max_players', models.IntegerField(default=16, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(128)])),
                ('status', models.CharField(choices=[('CR', 'created'), ('ON', 'on_going'), ('CO', 'completed')], default='CR', max_length=2, verbose_name='Tournament Status')),
                ('number_of_matches', models.IntegerField(default=0)),
                ('number_of_byes', models.IntegerField(default=0)),
                ('current_number_of_players', models.IntegerField(default=0)),
                ('max_tree_level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1_score', models.IntegerField(default=0)),
                ('player_2_score', models.IntegerField(default=0)),
                ('is_played', models.BooleanField(default=False)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_bye', models.BooleanField(default=False)),
                ('tree_level', models.IntegerField(default=0)),
                ('tree_node', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
