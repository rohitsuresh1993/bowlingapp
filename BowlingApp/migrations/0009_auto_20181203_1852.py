# Generated by Django 2.1.3 on 2018-12-04 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BowlingApp', '0008_auto_20181203_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bowlermatchstats',
            name='admin_id',
        ),
        migrations.RemoveField(
            model_name='bowlermatchstats',
            name='bowler_id',
        ),
        migrations.RemoveField(
            model_name='bowlermatchstats',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='bowlermatchstats',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='bowler',
            name='bowler_phone',
        ),
        migrations.RemoveField(
            model_name='referee',
            name='password',
        ),
        migrations.RemoveField(
            model_name='referee',
            name='ref_phone',
        ),
        migrations.DeleteModel(
            name='BowlerMatchStats',
        ),
    ]
