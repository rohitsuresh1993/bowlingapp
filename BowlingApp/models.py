from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class League(models.Model):
    league = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='league_profile')
    admin_id = models.AutoField(primary_key=True)
    league_email = models.EmailField(max_length=128)
    league_name = models.CharField(max_length=120)
    league_venue = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.league_name

class Referee(models.Model):
    referee=models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='refuser')
    ref_id=models.AutoField(primary_key=True)
    admin_id = models.ForeignKey('League', on_delete=models.CASCADE,related_name='reftoleague')
    ref_email=models.EmailField(max_length=128)
    ref_name = models.CharField(max_length=120)
    ref_address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    def __str__(self):
        return self.ref_name

class Bowler(models.Model):
    bowler1=models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='bowleruser')
    bowler_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey('League', on_delete=models.CASCADE,related_name='blrtoleague')
    bowler_name=models.TextField()
    bowler_email=models.EmailField(max_length=128)
    bowler_address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    avg_score=models.PositiveIntegerField(null=True,validators=[MaxValueValidator(300)])

    def __str__(self):
        return self.bowler_name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey('League', on_delete=models.CASCADE,related_name='teamtoleague')
    team_email=models.EmailField(max_length=128)
    team_name = models.TextField()
    tm_1 = models.ForeignKey('Bowler',on_delete=models.CASCADE,related_name='tm_1')
    tm_2 = models.ForeignKey('Bowler', on_delete=models.CASCADE,related_name='tm_2')
    tm_3 = models.ForeignKey('Bowler', on_delete=models.CASCADE,related_name='tm_3')
    team_avg=models.PositiveIntegerField(null=True,validators=[MaxValueValidator(900)])
    def __str__(self):
        return self.team_name

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    ref=models.ForeignKey('Referee', on_delete=models.CASCADE,related_name='reftomatch')
    admin_id = models.ForeignKey('League', on_delete=models.CASCADE,related_name='matchtoleague')
    team_1_id = models.ForeignKey('Team', on_delete=models.CASCADE,related_name='team_1')
    team_1_game_1_score=models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_1_game_2_score=models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_1_game_3_score = models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_1_total_score=models.PositiveIntegerField(validators=[MaxValueValidator(2700)],null=True)
    team_2_id = models.ForeignKey('Team', on_delete=models.CASCADE,related_name='team_2')
    team_2_game_1_score = models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_2_game_2_score = models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_2_game_3_score = models.PositiveIntegerField(validators=[MaxValueValidator(900)],null=True)
    team_2_total_score = models.PositiveIntegerField(validators=[MaxValueValidator(2700)],null=True)