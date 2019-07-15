from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from BowlingApp.forms import LeagueProfile, TeamStatQuery, RefProfile, PlayerStatQuery
from BowlingApp.models import Team, Bowler
from . import forms

# Create your views here.
def homepage(request):
    return render(request,
                  'homepage.html',
                  {
                       'title':'Home',
                       'heading':'ScoreKeeper',
                  }
                  )

def leaguelogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('lhome')
    else:
        form=AuthenticationForm()
    return render(request,
                  'leagueLogin.html',
                  {
                       'title':'League Login',
                       'heading':'Log in : League',
                       'form':form
                  }
                  )

def reflogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('refhome')
    else:
        form=AuthenticationForm()
    return render(request,
                  'refLogin.html',
                  {
                       'title':'Referee Login',
                       'heading':'Log in : Referee',
                       'form':form
                  }
                  )

def bowlerlogin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blrhome')
    else:
        form=AuthenticationForm()
    return render(request,
                  'bowlerLogin.html',
                  {
                       'title':'Bowler Login',
                       'heading':'Log in : Bowler',
                       'form':form
                  }
                  )

def leaguesignup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log the user in
            login(request, user)
            return redirect('lgprofile')
    else:
        form=UserCreationForm()
    return render(request,
                  'leagueSignup.html',
                  {
                      'title':'League Registration',
                      'heading':'Register your league',
                      'form': form
                  }
                  )

def refsignup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log the user in
            login(request, user)
            return redirect('refprofile')
    else:
        form=UserCreationForm()
    return render(request,
                  'refSignup.html',
                  {
                      'title':'Referee Registration',
                      'heading':'Register Referee',
                      'form': form
                  }
                  )

def bowlersignup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log the user in
            login(request, user)
            return redirect('blrprofile')
    else:
        form=UserCreationForm()
    return render(request,
                  'bowlerSignup.html',
                  {
                      'title':'Bowler Registration',
                      'heading':'Register Bowler',
                      'form': form
                  }
                  )

@login_required(login_url="/home/")
def leagueProfile(request):
    if request.method=='POST':
        form=LeagueProfile(request.POST)
        if form.is_valid():
            #save to db
            instance=form.save(commit=False)
            instance.admin_id=request.user.id
            instance.save()
            return redirect('lhome')
    else:
        form=LeagueProfile()
    return render(request,
                  'leagueProfile.html',
                  {
                      'title':'League Profile',
                      'heading':'Complete League Profile',
                      'form': form
                  }
                  )

@login_required(login_url="/home/")
def logout_view(request):
    if request.method=='POST':
        form = AuthenticationForm()
        logout(request)
    return render(request,
                      'loggedout.html',
                      {
                          'title':'Logged out',
                          'heading':'Successfully logged out'
                      }
                      )

@login_required(login_url="/home/")
def checkout(request):
    return render(request,
                  'checkoutPage.html',
                  {
                      'title':'Check out',
                      'heading':'Checkout',
                  }
                  )

@login_required(login_url="/home/")
def matchRecord(request):
    if request.method=='POST':
        form=forms.MatchRecord(request.POST)
        if form.is_valid():
            #save to db
            instance=form.save(commit=False)
            instance.save()
            return redirect('refhome')
    else:
        form=forms.MatchRecord()
    return render(request,
                  'matchRecord.html',
                  {
                      'title':'Match Record',
                      'heading':'Enter Scores',
                      'form':form
                  }
                  )

@login_required(login_url="/home/")
def refprofile(request):
    if request.method=='POST':
        form=RefProfile(request.POST)
        if form.is_valid():
            #save to db
            instance=form.save(commit=False)
            instance.referee = request.user
            instance.save()
            return redirect('refhome')
    else:
        form=RefProfile()
    return render(request,
                  'refProfile.html',
                  {
                      'title':'Referee Profile',
                      'heading':'Complete Referee Profile',
                      'form': form
                  }
                  )

@login_required(login_url="/home/")
def teamsignup(request):
    if request.method=='POST':
        form=forms.CreateTeam(request.POST)
        if form.is_valid():
            #save to db
            instance=form.save(commit=False)
            instance.save(force_insert=True)
            return redirect('blrhome')
    else:
        form=forms.CreateTeam()
    return render(request,
                  'teamSignup.html',
                  {
                      'title':'Team Signup',
                      'heading':'Create your team',
                      'form':form
                  }
                  )

@login_required(login_url="/home/")
def leaguehome(request):
    return render(request,
                  'leagueadminHome.html',
                  {
                      'title':'League Home',
                      'heading':'Welcome!',
                  }
                  )

@login_required(login_url="/home/")
def refhome(request):
    return render(request,
                  'refHome.html',
                  {
                      'title':'Referee Home',
                      'heading':'Welcome!',
                  }
                  )

@login_required(login_url="/home/")
def bowlerhome(request):
    return render(request,
                  'bowlerHome.html',
                  {
                      'title':'Bowler Home',
                      'heading':'Welcome!',
                  }
                  )

@login_required(login_url="/home/")
def bowlerprofile(request):
    if request.method=='POST':
        form=forms.BowlerProfile(request.POST)
        if form.is_valid():
            #save to db
            instance=form.save(commit=False)
            instance.bowler1=request.user
            instance.save()
            return redirect('blrhome')
    else:
        form=forms.BowlerProfile()
    return render(request,
                  'bowlerProfile.html',
                  {
                      'title':'Bowler Signup',
                      'heading':'Bowler Profile',
                      'form':form
                  }
                  )

@login_required(login_url="/home/")
def teamstats(request):
        if request.method == 'POST':
            form = TeamStatQuery(request.POST)
            if form.is_valid():
                adminid=form.cleaned_data.get('admin_id')
                t1email = form.cleaned_data.get('team_1')
                t2email = form.cleaned_data.get('team_2')
                t1=Team.objects.filter(admin_id=adminid,team_email=t1email).values('team_name','team_avg')
                t2 = Team.objects.filter(admin_id=adminid, team_email=t2email).values('team_name', 'team_avg')
                form = forms.TeamStatQuery()
                return render(request,
                              'teamstatQuery.html',
                              {
                                  'title': 'Team Stats',
                                  'heading': 'Stat Center',
                                  'form': form,
                                  't1':t1,
                                  't2':t2,
                              }
                              )
        else:
            form = forms.TeamStatQuery()
            return render(request,
                          'teamstatQuery.html',
                          {
                              'title': 'Team Stats',
                              'heading': 'Stat Center',
                              'form': form
                          }
                          )

@login_required(login_url="/home/")
def playerstats(request):
        if request.method == 'POST':
            form = PlayerStatQuery(request.POST)
            if form.is_valid():
                adminid=form.cleaned_data.get('admin_id')
                p1email = form.cleaned_data.get('bowler_1')
                p2email = form.cleaned_data.get('bowler_2')
                p1=Bowler.objects.filter(admin_id=adminid,bowler_email=p1email).values('bowler_name','avg_score')
                p2 = Bowler.objects.filter(admin_id=adminid, bowler_email=p2email).values('bowler_name', 'avg_score')
                form = forms.PlayerStatQuery()
                return render(request,
                              'playerstatQuery.html',
                              {
                                  'title': 'Team Stats',
                                  'heading': 'Stat Center',
                                  'form': form,
                                  'p1':p1,
                                  'p2':p2,
                              }
                              )
        else:
            form = forms.PlayerStatQuery()
            return render(request,
                          'playerstatQuery.html',
                          {
                              'title': 'Team Stats',
                              'heading': 'Stat Center',
                              'form': form
                          }
                          )