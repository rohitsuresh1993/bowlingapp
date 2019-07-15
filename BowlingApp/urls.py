"""Bowling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from BowlingApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.homepage, name="home"),
    url(r'^home/$',views.homepage, name="home"),
    url(r'^leaguelogin/$',views.leaguelogin, name="lglogin"),
    url(r'^reflogin/$',views.reflogin, name="reflogin"),
    url(r'^bowlerlogin/$',views.bowlerlogin, name="blrlogin"),
    url(r'^leaguesignup/$',views.leaguesignup, name="lgsup"),
    url(r'^leagueprofile/$', views.leagueProfile, name="lgprofile"),
    url(r'^refereeprofile/$', views.refprofile, name="refprofile"),
    url(r'^bowlerprofile/$', views.bowlerprofile, name="blrprofile"),
    url(r'^teamstats/$',views.teamstats,name="tstats"),
    url(r'^playerstats/$',views.playerstats,name="pstats"),
    url(r'^checkout/$',views.checkout,name="checkout"),
    url(r'^matchrecord/$',views.matchRecord,name="matchrec"),
    url(r'^refsignup/$',views.refsignup,name="refsup"),
    url(r'^teamsignup/$',views.teamsignup,name="tsup"),
    url(r'^bowlersignup$',views.bowlersignup,name="bsup"),
    url(r'^leaguehome/$',views.leaguehome,name="lhome"),
    url(r'^refhome/$',views.refhome,name="refhome"),
    url(r'^bowlerhome/$',views.bowlerhome,name="blrhome"),
    url(r'^logout/$',views.logout_view,name='logout')
]

urlpatterns += staticfiles_urlpatterns()