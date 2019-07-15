# Generated by Django 2.1.3 on 2018-12-03 21:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BowlingApp', '0006_auto_20181203_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_avg',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(300)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bowlermatchstats',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blrstatstoleague', to='BowlingApp.League'),
        ),
        migrations.AlterField(
            model_name='bowlermatchstats',
            name='bowler_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blrstatstoblr', to='BowlingApp.Bowler'),
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tmstattoleague', to='BowlingApp.League'),
        ),
    ]
