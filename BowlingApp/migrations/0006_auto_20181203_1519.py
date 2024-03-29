# Generated by Django 2.1.3 on 2018-12-03 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BowlingApp', '0005_league_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='match_winner',
        ),
        migrations.AlterField(
            model_name='bowler',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blrtoleague', to='BowlingApp.League'),
        ),
        migrations.AlterField(
            model_name='match',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchtoleague', to='BowlingApp.League'),
        ),
        migrations.AlterField(
            model_name='referee',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reftoleague', to='BowlingApp.League'),
        ),
        migrations.AlterField(
            model_name='team',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamtoleague', to='BowlingApp.League'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tm_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tm_1', to='BowlingApp.Bowler'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tm_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tm_2', to='BowlingApp.Bowler'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tm_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tm_3', to='BowlingApp.Bowler'),
        ),
    ]
