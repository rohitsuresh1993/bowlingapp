# Generated by Django 2.1.3 on 2018-12-04 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BowlingApp', '0017_remove_match_reffie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='captain',
        ),
    ]
