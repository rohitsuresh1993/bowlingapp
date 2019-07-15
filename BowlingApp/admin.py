from django.contrib import admin
from .models import League
from .models import Referee
from .models import Team
from .models import Bowler
from .models import Match

# Register your models here.
admin.site.register(League)
admin.site.register(Referee)
admin.site.register(Team)
admin.site.register(Bowler)
admin.site.register(Match)
