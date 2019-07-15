from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class LeagueProfile(forms.ModelForm):
    class Meta:
        model=models.League
        fields=[
            'league_name',
            'league_email',
            'league_venue',
            'city',
            'state',
            'zip'
        ]
        labels={
            'league_name':_('League Name'),
            'league_email':_('Email'),
            'league_venue':_('Venue'),
            'city':_('City'),
            'state':_('State'),
            'zip':_('Zipcode'),
        }

class CreateTeam(forms.ModelForm):
    class Meta:
        model=models.Team
        fields=[
            'admin_id',
            'team_email',
            'team_name',
            'tm_1',
            'tm_2',
            'tm_3',
        ]
        labels={
            'admin_id':_('League'),
            'team_email':_('Email'),
            'team_name':_('Team Name'),
            'tm_1':_('Team Member 1'),
            'tm_2':_('Team Member 2'),
            'tm_3':_('Team Member 3'),
        }

class MatchRecord(forms.ModelForm):
    class Meta:
        model=models.Match
        fields=[
            'admin_id',
            'ref',
            'team_1_id',
            'team_2_id',
            'team_1_game_1_score',
            'team_1_game_2_score',
            'team_1_game_3_score',
            'team_2_game_1_score',
            'team_2_game_2_score',
            'team_2_game_3_score',
        ]
        labels={
            'admin_id':_('League'),
            'ref':_('Referee'),
            'team_1_id':_('Team 1'),
            'team_2_id':_('Team 2'),
            'team_1_game_1_score':_('Team 1 score: Game 1'),
            'team_1_game_2_score':_('Team 1 score: Game 2'),
            'team_1_game_3_score':_('Team 1 score: Game 3'),
            'team_2_game_1_score':_('Team 2 score: Game 1'),
            'team_2_game_2_score':_('Team 2 score: Game 2'),
            'team_2_game_3_score':_('Team 2 score: Game 3'),
        }

class TeamStatQuery(forms.ModelForm):
    class Meta:
        model=models.Team
        fields=['admin_id']
        labels={'admin_id':'Select League'}

    team_1 = forms.EmailField(max_length=128,required=True,label="Your team's email")
    team_2 = forms.EmailField(max_length=128,required=True,label="Opposition team's email")

class PlayerStatQuery(forms.ModelForm):
    class Meta:
        model=models.Bowler
        fields=['admin_id']
        labels={'admin_id':'Select League'}

    bowler_1 = forms.EmailField(max_length=128,required=True,label='Player 1 email')
    bowler_2 = forms.EmailField(max_length=128,required=True,label='Player 2 email')

class RefProfile(forms.ModelForm):
    class Meta:
        model = models.Referee
        fields = [
            'admin_id',
            'ref_name',
            'ref_email',
            'ref_address',
            'city',
            'state',
            'zip'
        ]
        labels = {
            'admin_id':_('League'),
            'ref_name': _('Name'),
            'ref_email': _('Email'),
            'ref_address': _('Address'),
            'city': _('City'),
            'state': _('State'),
            'zip': _('Zipcode'),
        }

class BowlerProfile(forms.ModelForm):
    class Meta:
        model = models.Bowler
        fields = [
            'admin_id',
            'bowler_name',
            'bowler_email',
            'bowler_address',
            'city',
            'state',
            'zip'
        ]
        labels = {
            'admin_id':_('League'),
            'bowler_name': _('Name'),
            'bowler_email': _('Email'),
            'bowler_address': _('Address'),
            'city': _('City'),
            'state': _('State'),
            'zip': _('Zipcode'),
        }