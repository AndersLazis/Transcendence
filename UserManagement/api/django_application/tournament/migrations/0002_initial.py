# Generated by Django 5.0.6 on 2024-08-21 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tournaments', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_tournaments', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='tournamentlobby',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_participations', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='tournamentlobby',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lobby', to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='player_1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournamentmatch_player_1_matches', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='player_2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournamentmatch_player_2_matches', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_won_matches', to='user_profile.userprofile'),
        ),
        migrations.AddConstraint(
            model_name='tournamentlobby',
            constraint=models.UniqueConstraint(fields=('tournament', 'player'), name='unique_tournament_player'),
        ),
    ]
