# Generated by Django 2.1.3 on 2018-12-03 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BowlingApp', '0007_auto_20181203_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='bowler',
            name='bowler1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bowleruser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referee',
            name='referee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
